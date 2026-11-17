const kohde = document.getElementById("target");

const ensimmainen = document.createElement("li");
ensimmainen.textContent = "First item";
kohde.appendChild(ensimmainen);

const toinen = document.createElement("li");
toinen.textContent = "Second item";
toinen.classList.add("my-item");
kohde.appendChild(toinen);

const kolmas = document.createElement("li");
kolmas.textContent = "Third item";
kohde.appendChild(kolmas);