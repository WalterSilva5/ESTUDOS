class Pessoa {
  _nome: string;
  get getNome() {
    return this._nome
  }
  set setNome(nome: string) {
    this._nome = nome
  }
}

let teste = new Pessoa()
teste.setNome = "walter"
console.log(teste)