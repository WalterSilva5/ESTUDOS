var Pessoa = /** @class */ (function () {
    function Pessoa() {
    }
    Object.defineProperty(Pessoa.prototype, "getNome", {
        get: function () {
            return this._nome;
        },
        enumerable: false,
        configurable: true
    });
    Object.defineProperty(Pessoa.prototype, "setNome", {
        set: function (nome) {
            this._nome = nome;
        },
        enumerable: false,
        configurable: true
    });
    return Pessoa;
}());
var teste = new Pessoa();
teste.setNome = "walter";
console.log(teste);
