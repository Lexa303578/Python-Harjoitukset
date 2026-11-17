function heitaNoppaa(sivut) {
  return Math.floor(Math.random() * sivut) + 1;
}

const sivut = Number(prompt("Montako sivua nopassa on?"));

if (isNaN(sivut) || sivut < 1) {
  alert("Anna kelvollinen sivujen määrä (vähintään 1).");
} else {
  const lista = document.getElementById("heitot");
  let tulos;

  do {
    tulos = heitaNoppaa(sivut);

    const li = document.createElement("li");
    li.textContent = tulos;
    lista.appendChild(li);
  } while (tulos !== sivut);
}