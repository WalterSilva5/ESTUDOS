interface Transporte {
  criarViagem(distancia: number): Viagem
}

class Viagem {
  distancia: number;
  constructor(distancia: number) {
    this.distancia = distancia
  }
}

class TransporteMaritimo implements Transporte {
  veiculo = "barco"
  criarViagem(distancia: number): Viagem{
    return new Viagem(distancia)
  }
}

let viagemDeBarco = new TransporteMaritimo().criarViagem(100)

console.log(viagemDeBarco)