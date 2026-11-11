let heitot = parseInt(prompt('Montako noppaa heitetään?'));

let summa = 0;

for (let i = 0; i < heitot; i++) {
  let silmaluku = Math.floor(Math.random() * 6) + 1;
  summa = summa + silmaluku;
}

document.getElementById('tulos').textContent = `Heittojen summa on ${summa}`;