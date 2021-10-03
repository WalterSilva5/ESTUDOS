interface Pessoa {
  nome: string
}

class Pessoa implements Pessoa {
  nome = 'walter'
}

var teste = new Pessoa()
console.log(teste)

