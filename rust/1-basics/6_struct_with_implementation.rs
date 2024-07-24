struct Retângulo {
    largura: u32,
    altura: u32,
}

struct Ciruculo {
    raio: f64,
}

trait Forma {
    fn calcular_area(&self) -> f64;
}

impl Forma for Retângulo {
    fn calcular_area(&self) -> f64 {
        f64::from(self.largura * self.altura)
    }
}

impl Forma for Ciruculo {
    fn calcular_area(&self) -> f64 {
        std::f64::consts::PI * self.raio * self.raio
    }
}

fn main() {
    let retangulo = Retângulo {
        largura: 10,
        altura: 5,
    };

    let ciruculo = Ciruculo {
        raio: 7.0,
    };

    println!("Área do retângulo: {}", retangulo.calcular_area());
    println!("Área do Ciruculo: {}", ciruculo.calcular_area());
}