const tulos = document.getElementById("tulos");

for (let i = 1; i <= 5; i++) {
  const numero = prompt("Anna numero " + i + "/5:");
  console.log("Kierros", i, "arvo:", numero);
  const p = document.createElement("p");
  p.textContent = numero;
  tulos.appendChild(p);
}