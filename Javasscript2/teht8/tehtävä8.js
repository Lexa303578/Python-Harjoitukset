function concat(taulukko) {
  let tulos = "";

  for (const alkio of taulukko) {
    tulos = tulos + alkio;
  }

  return tulos;
}

const nimet = ["Johnny", "DeeDee", "Joey", "Marky"];

document.getElementById("tulos").textContent = concat(nimet);