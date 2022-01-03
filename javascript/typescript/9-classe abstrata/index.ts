abstract class Pessoa{
  nome: string
}

class Atleta extends Pessoa{
  esporte: string;
  constructor() {
    super()
  }
}

var teste = new Atleta()
teste.nome = "walter"

console.log(teste)