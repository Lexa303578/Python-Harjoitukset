let ensimmainen = parseInt(prompt('Anna ensimmäinen kokonaisluku:'));
let toinen = parseInt(prompt('Anna toinen kokonaisluku:'));
let kolmas = parseInt(prompt('Anna kolmas kokonaisluku:'));

let summa = ensimmainen + toinen + kolmas;
let tulo = ensimmainen * toinen * kolmas;
let keskiarvo = summa / 3;

document.getElementById('summa').textContent = `Summa: ${summa}`;
document.getElementById('tulo').textContent = `Tulo: ${tulo}`;
document.getElementById('keskiarvo').textContent = `Keskiarvo: ${keskiarvo}`;