const kentta = document.querySelector("input");
const nappi = document.querySelector("button");
const tulos = document.getElementById("result");

nappi.addEventListener("click", function () {
  const lauseke = kentta.value.replaceAll(" ", "");
  let vastaus;

  if (lauseke.includes("+")) {
    const osat = lauseke.split("+");
    vastaus = parseInt(osat[0]) + parseInt(osat[1]);
  } else if (lauseke.includes("-")) {
    const osat = lauseke.split("-");
    vastaus = parseInt(osat[0]) - parseInt(osat[1]);
  } else if (lauseke.includes("*")) {
    const osat = lauseke.split("*");
    vastaus = parseInt(osat[0]) * parseInt(osat[1]);
  } else if (lauseke.includes("/")) {
    const osat = lauseke.split("/");
    vastaus = parseInt(osat[0]) / parseInt(osat[1]);
  } else {
    vastaus = "Virheellinen lauseke";
  }

  tulos.textContent = vastaus;
});