// importa o modulo http
var http = require("http")

// cria um servidor http na porta 80
http.createServer(
    function(requisicao, resposta) {
        resposta.end("<h1>SERVIDOR FUNCIONANDO!</h1>")
    }
).listen(80)