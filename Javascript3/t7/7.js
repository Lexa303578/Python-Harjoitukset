const trigger = document.getElementById("trigger");
const kuva = document.getElementById("target");

trigger.addEventListener("mouseover", function () {
  kuva.src = "img/picB.jpg";
});

trigger.addEventListener("mouseout", function () {
  kuva.src = "img/picA.jpg";
});