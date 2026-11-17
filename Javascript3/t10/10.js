const lomake = document.querySelector("form");
const kentat = document.querySelectorAll('input[type="text"]');
const kohde = document.getElementById("target");

lomake.addEventListener("submit", function (event) {
  event.preventDefault();

  const etunimi = kentat[0].value;
  const sukunimi = kentat[1].value;

  kohde.textContent = "Your name is " + etunimi + " " + sukunimi;
});