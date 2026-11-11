let lasketaanko = confirm('Lasketaanko neliöjuuri?');

let tulos;

if (lasketaanko) {
  let luku = parseFloat(prompt('Anna luku:'));

  if (luku < 0) {
    tulos = 'Negatiivisen luvun neliöjuurta ei ole määritelty';
  } else {
    tulos = `Luvun ${luku} neliöjuuri on ${Math.sqrt(luku)}`;
  }
} else {
  tulos = 'Neliöjuurta ei lasketa.';
}

document.getElementById('tulos').textContent = tulos;