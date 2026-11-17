const kentat = document.querySelectorAll("input");
const valinta = document.querySelector("select");
const nappi = document.querySelector("button");
const tulos = document.getElementById("result");

nappi.addEventListener("click", function () {
  const a = Number(kentat[0].value);
  const b = Number(kentat[1].value);
  const operaatio = valinta.value;

  let vastaus;

  switch (operaatio) {
    case "add":
      vastaus = a + b;
      break;
    case "sub":
      vastaus = a - b;
      break;
    case "multi":
      vastaus = a * b;
      break;
    case "div":
      vastaus = a / b;
      break;
  }

  tulos.textContent = vastaus;
});