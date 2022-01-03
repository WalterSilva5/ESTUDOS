class Pessoa {
  nome: string;
  private idade: number;
  //modifiers can be public private and protected and readonly
  constructor(nome: string, idade: number) {
    this.nome = nome;
    this.idade = idade;
  }
  nomeCompleto(): void{
    console.log(this.nome);
  }
}

class Atleta extends Pessoa{
  esporte: string;
  constructor(nome: string, idade: number, esporte: string) {
    super(nome, idade);
    this.esporte = esporte;
  }
}

var pes = new Atleta("walter", 24, "futebol")
console.log(pes)
pes.nomeCompleto()