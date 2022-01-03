"use strict";
var Cadeira = /** @class */ (function () {
    function Cadeira() {
        this.pernas = 4;
        this.largura = 60;
    }
    return Cadeira;
}());
var FabricaDeCadeiras = /** @class */ (function () {
    function FabricaDeCadeiras() {
    }
    FabricaDeCadeiras.prototype.criarCadeira = function () {
        return new Cadeira();
    };
    return FabricaDeCadeiras;
}());
var teste = new FabricaDeCadeiras().criarCadeira();
console.log(teste);
