interface CadeiraAbstrata{
  pernas: number,
  largura: number
}

interface FabricaDeMoveis{
  criarCadeira(): CadeiraAbstrata;
}

class Cadeira implements CadeiraAbstrata{
  pernas = 4;
  largura = 60;
}

class FabricaDeCadeiras implements FabricaDeMoveis{
  criarCadeira(): Cadeira{
    return new Cadeira()
  }
}

let teste = new FabricaDeCadeiras().criarCadeira()
console.log(teste)