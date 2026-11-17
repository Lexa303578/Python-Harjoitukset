const numerot = [];

while (true) {
  const numero = Number(prompt("Anna numero (0 lopettaa):"));

  if (numero === 0) {
    break;
  }

  numerot.push(numero);
}

numerot.sort(function (a, b) {
  return b - a;
});

for (const numero of numerot) {
  console.log(numero);
}