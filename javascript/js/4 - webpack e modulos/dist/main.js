(() => {
    var o, e = {
            847: o => {
                o.exports = {
                    pessoa: {
                        nome: "walter"
                    }
                }
            }
        },
        r = {};
    o = function o(s) {
        var t = r[s];
        if (void 0 !== t) return t.exports;
        var n = r[s] = {
            exports: {}
        };
        return e[s](n, n.exports, o), n.exports
    }(847), console.log(o.pessoa.nome)
})();