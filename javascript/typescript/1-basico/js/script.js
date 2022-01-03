"use strict";
function somar() {
    var t1 = document.getElementById("v1");
    var t2 = document.getElementById("v2");
    fazerSoma(Number(t1.value), Number(t2.value));
}
function fazerSoma(t1, t2) {
    return console.log(t1 + t2);
}
