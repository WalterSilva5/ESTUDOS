"use strict";
var Viagem = /** @class */ (function () {
    function Viagem(distancia) {
        this.distancia = distancia;
    }
    return Viagem;
}());
var TransporteMaritimo = /** @class */ (function () {
    function TransporteMaritimo() {
        this.veiculo = "barco";
    }
    TransporteMaritimo.prototype.criarViagem = function (distancia) {
        return new Viagem(distancia);
    };
    return TransporteMaritimo;
}());
var viagemDeBarco = new TransporteMaritimo().criarViagem(100);
console.log(viagemDeBarco);
