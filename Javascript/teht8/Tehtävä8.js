let alkuvuosi = parseInt(prompt('Anna alkuvuosi:'));
let loppuvuosi = parseInt(prompt('Anna loppuvuosi:'));

let rivit = '';

for (let vuosi = alkuvuosi; vuosi <= loppuvuosi; vuosi++) {
  if ((vuosi % 4 === 0 && vuosi % 100 !== 0) || vuosi % 400 === 0) {
    rivit += `<li>${vuosi}</li>`;
  }
}

document.getElementById('lista').innerHTML = rivit;