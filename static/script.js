
const bouton0 = document.querySelector('div.day0');
const bouton1 = document.querySelector('div.day1');
const bouton2 = document.querySelector('div.day2');
const bouton3 = document.querySelector('div.day3');
const bouton4 = document.querySelector('div.day4');
const bouton5 = document.querySelector('div.day5');
const bouton6 = document.querySelector('div.day6');
// Sélectionne l'élément actif initialement
var Actif = document.querySelector('.date .actif');



bouton0.addEventListener('click', function() {Switch(bouton0)});
bouton1.addEventListener('click', function() {Switch(bouton1)});
bouton2.addEventListener('click', function() {Switch(bouton2)});
bouton3.addEventListener('click', function() {Switch(bouton3)});
bouton4.addEventListener('click', function() {Switch(bouton4)});
bouton5.addEventListener('click', function() {Switch(bouton5)});
bouton6.addEventListener('click', function() {Switch(bouton6)});




function Switch(bouton) {
    // Supprime la classe 'actif' de l'élément actuellement actif
    if (Actif) {
        Actif.classList.remove('actif');
    }
    localStorage.setItem('bouton',bouton.classList.toString());
    console.log(bouton.classList);
    // Ajoute la classe 'actif' au bouton
    bouton.classList.add('actif');
    
    

    // Met à jour la variable Actif pour pointer vers le nouvel élément actif
    Actif = bouton;

    // Envoie la requête POST avec fetch
    
}

const savedActif = localStorage.getItem('bouton');
const Actif_btn = document.querySelector('div.'+savedActif)
if(Actif_btn){
    Switch(Actif_btn)};
