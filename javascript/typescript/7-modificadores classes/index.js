var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Pessoa = /** @class */ (function () {
    function Pessoa(nome, idade) {
        this.nome = nome;
        this.idade = idade;
    }
    Pessoa.prototype.nomeCompleto = function () {
        console.log(this.nome);
    };
    return Pessoa;
}());
var Atleta = /** @class */ (function (_super) {
    __extends(Atleta, _super);
    function Atleta(nome, idade, esporte) {
        var _this = _super.call(this, nome, idade) || this;
        _this.esporte = esporte;
        return _this;
    }
    return Atleta;
}(Pessoa));
var pes = new Atleta("walter", 24, "futebol");
console.log(pes);
pes.nomeCompleto();
