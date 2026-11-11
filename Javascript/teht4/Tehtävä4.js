let nimi = prompt('Mikä on nimesi?');

let luku = Math.floor(Math.random() * 4) + 1;

let tupa;

switch (luku) {
  case 1:
    tupa = 'Rohkelikko';
    break;
  case 2:
    tupa = 'Luihuinen';
    break;
  case 3:
    tupa = 'Puuskupuh';
    break;
  default:
    tupa = 'Korpinkynsi';
}

document.getElementById('tulos').textContent = `${nimi}, olet ${tupa}.`;