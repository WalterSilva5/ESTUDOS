const app = require('express')

app.get("/", function(req, res) {
    res.send("<h1>INDEX DO PROJETO</h1>");
});
app.get("/teste", function(req, res) {
    res.send("<h1>PAGINA DE TESTE</h1>")
})


app.listen(80, function(erro) {
    if (erro) {
        console.log("ocorreu um erro");
    } else {
        console.log("servidor funcionando");
    }
});