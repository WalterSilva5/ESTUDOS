function somar() {
  let t1 = document.getElementById("v1") as HTMLInputElement;
  let t2 = document.getElementById("v2") as HTMLInputElement;
  fazerSoma(Number(t1.value), Number(t2.value));
}

function fazerSoma(t1: number, t2: number) {
  return console.log(t1 + t2);
}