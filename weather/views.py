from django.shortcuts import render
from .models import *

def day(request):
    predict = days(30)
    return render(request, 'index.html', context=predict)
# Create your views here.

def day1(request):
    predict = days(20)
    return render(request, 'index.html', context=predict)

def day2(request):
    predict = days(10)
    return render(request, 'index.html', context=predict)

def hebdo(jour):
    sem = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    hebdo = [jour]
    n = sem.index(jour)
    for i in range(5):
        hebdo.append(sem[(n+i+2)%7])
    
    return hebdo


def days(n):
    maintenant = datetime.datetime.now() 
    futur = maintenant + datetime.timedelta(hours=30-n)
    jour = maintenant.strftime('%A').capitalize()
    
    predict = {'date': futur.strftime('%A, %d %B %H:%M').capitalize, 
                'hebdo': hebdo(jour)}
    
    for parm in parms+['rose']:
        pred1 = list(WeatherPredict.objects.values_list(parm).order_by('-id')[n])[0]
        pred2 = list(WeatherPredict.objects.values_list(parm).order_by('-id')[n-1])[0]
        if parm =='precipitation':
            predict[parm] = [round(pred1, 2), round(pred1-pred2)]
            continue
        predict[parm] = [int(pred1), int(pred1-pred2)]

    fparams = []
    for i in range(1,5):
        L = list(WeatherPredict.objects.values_list('temperature', 'temperation_soil', 'humidity').order_by('-id')[n-i])
        L.append(int(maintenant.strftime('%H'))+i)
        fparams.append([int(i) for i in L])

    predict['fparams'] = fparams
    predict['sante'] = random.choice(conseil_sante(predict['temperature'][0], predict['humidity'][0], predict['wind_speed'][0]))
    #print(predict['fparams'])
    
    return predict

import locale
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')


def conseil_sante():
    pass

def vetem():
    pass

def activites():
    params = ['parapluie', 'exterieur', 'uv', 'conduite']
    for param in params:
        pass
    pass


    

import random
import numpy as np
import math
from joblib import load, dump
import sched
import time
import datetime

data = load('./save_model/dataset.joblib')

def calcul_point_de_rosee(temperature, humidite_relative):
    # Constantes
    a = 17.27
    b = 237.7

    gamma = (a * temperature) / (b + temperature) + math.log(humidite_relative / 100.0)
    point_de_rosee = (b * gamma) / (a - gamma)
    return point_de_rosee
    


def generate_weather_data():
    dl = []
    for i in range(1,2):
        weather_data = [
            data['Temperature'].iloc[-i],
            data['Precipitation Total'].iloc[-i],
            data['Relative Humidity'].iloc[-i],
            data['Wind Speed'].iloc[-i],
            data['UV Radiation'].iloc[-i],
            data['Mean Sea Level Pressure'].iloc[-i],
            data['Evapotranspiration'].iloc[-i],
            data['Soil Temperature'].iloc[-i],
            data['Cloud Cover Low'].iloc[-i]
        ]
        dl.append(weather_data)
    
    return dl

def weather_view(request):
    weather_data = generate_weather_data()
    context = {'weather_data': weather_data}
    return render(request, 'index.html', context)


def add_data(n=1):
    t = load('./save_model/time.joblib')
    for i in range(1,n+1):
        donnee = WeatherData.objects.create(
                temperature = data['Temperature'].iloc[t+i],
                precipitation = data['Precipitation Total'].iloc[t+i],
                humidity = data['Relative Humidity'].iloc[t+i],
                wind_speed = data['Wind Speed'].iloc[t+i],
                uv = data['UV Radiation'].iloc[t+i],
                pressure = data['Mean Sea Level Pressure'].iloc[t+i],
                evapotranspiration = data['Evapotranspiration'].iloc[t+i],
                temperation_soil = data['Soil Temperature'].iloc[t+i],
                couverture = data['Cloud Cover Low'].iloc[t+i]
            )
        donnee.save()
    t += i
    dump(t, './save_model/time.joblib')

#add_data(1)
parms = parms = ['temperature','precipitation', 'humidity', 'wind_speed',
                     'couverture', 'uv','pressure','evapotranspiration', 'temperation_soil']
def prediction():
    prediction = {}
    
    for parm in parms:
        model = load(f'./save_model/model_{parm}.joblib')
        x_pred = np.array(list(WeatherData.objects.values_list(parm).order_by('-id')[:10])).transpose()
        pred = model.predict(x_pred)[0,0]
        #prediction.append(model.predict(x_pred)[0,0])
        #if pred < 0 and parm not in ['temperature', 'temperation_soil']:
        #
        # pred = 0
        
        prediction[parm] = pred
    
    
    rose = calcul_point_de_rosee(prediction['temperature'], prediction['humidity'])
    prediction['rose'] = rose    
    predict = WeatherPredict.objects.create(**prediction)     
    predict.save()     
    
    return


def futur_predict(h):
    
    for i in range(1,h+1):
        prediction = {}
        for parm in parms:
            if i < 10:
                x_pred =  np.array(list(WeatherData.objects.values_list(parm).order_by('-id')[:10-i]) + list(WeatherData.objects.values_list(parm).order_by('-id')[:i])).transpose()
            else:
                x_pred =  np.array(list(WeatherPredict.objects.values_list(parm).order_by('-id')[:10]))
                
            model = load(f'./save_model/model_{parm}.joblib')
            pred = model.predict(x_pred)[0,0]
            
            #if pred < 0 and parm not in ['temperature', 'temperation_soil']:
            #    pred = 0
        
            prediction[parm] = pred
        
        rose = calcul_point_de_rosee(prediction['temperature'], prediction['humidity'])
        prediction['rose'] = rose
        predict = WeatherPredict.objects.create(**prediction)     
        predict.save()   

#add_data(10)
#futur_predict(24)

planificateur = sched.scheduler(time.time, time.sleep)

def planifier_execution():
    planificateur.enter(300,1, planifier_execution)
    add_data(1)
    
#planifier_execution()
#planificateur.run()


def conseil_sante(temperature, humidity, wind_speed, weather_conditions='sun'):

    advice = []

    if temperature > 30:
        advice.append("Il fait très chaud dehors. Assurez-vous de rester hydraté et de rester au frais.")
    elif temperature < 0:
        advice.append("Il fait très froid dehors. Habillez-vous chaudement et évitez de rester dehors trop longtemps.")
    
    if humidity > 80:
        advice.append("L'humidité est élevée. Assurez-vous de vous protéger contre les maladies respiratoires.")
    
    if wind_speed > 10:
        advice.append("Il y a beaucoup de vent. Tenez-vous à l'abri si possible et assurez-vous que vos objets personnels sont sécurisés.")
    
    if 'rain' in weather_conditions.lower():
        advice.append("Il pleut. Prenez un parapluie ou un imperméable et faites attention aux surfaces glissantes.")

    if 'snow' in weather_conditions.lower():
        advice.append("Il neige. Soyez prudent sur les routes et assurez-vous de porter des vêtements chauds.")

    return advice

