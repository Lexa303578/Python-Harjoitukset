const numerot = [];

while (true) {
  const syote = prompt("Anna numero:");

  if (syote === null) {
    break;
  }

  const numero = Number(syote);

  if (isNaN(numero)) {
    continue;
  }

  if (numerot.includes(numero)) {
    alert("Numero " + numero + " on jo annettu.");
    break;
  }

  numerot.push(numero);
}

numerot.sort(function (a, b) {
  return a - b;
});

for (const numero of numerot) {
  console.log(numero);
}