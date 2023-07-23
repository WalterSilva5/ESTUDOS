function testarNome(classe: any) {
  console.log(classe)
}


@testarNome
class Pessoateste {
  nome: string;
  constructor(nome: string) {
    this.nome = nome;
  }
}


let pessoa = new Pessoateste("walter")