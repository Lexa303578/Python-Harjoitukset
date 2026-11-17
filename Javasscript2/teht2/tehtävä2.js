const lista = document.getElementById("osallistujat");

const maara = parseInt(prompt("How many participants?"));
const nimet = [];

for (let i = 1; i <= maara; i++) {
  const nimi = prompt("Enter the name of participant " + i + "/" + maara + ":");
  nimet.push(nimi);
}

nimet.sort(function (a, b) {
  return a.localeCompare(b, "fi");
});

for (const nimi of nimet) {
  const li = document.createElement("li");
  li.textContent = nimi;
  lista.appendChild(li);
}