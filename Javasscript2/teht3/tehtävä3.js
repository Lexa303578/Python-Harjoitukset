const lista = document.getElementById("koirat");
const nimet = [];

for (let i = 1; i <= 6; i++) {
  const nimi = prompt("Enter the name of dog " + i + "/6:");
  nimet.push(nimi);
}

nimet.sort(function (a, b) {
  return b.localeCompare(a, "fi");
});

for (const nimi of nimet) {
  const li = document.createElement("li");
  li.textContent = nimi;
  lista.appendChild(li);
}