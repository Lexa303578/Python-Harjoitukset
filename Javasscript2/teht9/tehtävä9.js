function even(taulukko) {
  const parilliset = [];

  for (const luku of taulukko) {
    if (luku % 2 === 0) {
      parilliset.push(luku);
    }
  }

  return parilliset;
}

const luvut = [2, 7, 4, 9, 10, 15, 8];
const parilliset = even(luvut);

console.log("Alkuperäinen taulukko:", luvut);
console.log("Parilliset luvut:", parilliset);