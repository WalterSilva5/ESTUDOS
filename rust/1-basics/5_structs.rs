struct Rectangle {
    largura: u32,
    altura: u32,
}

impl Rectangle {
    fn calcular_area(&self) -> u32 {
        self.largura * self.altura
    }

    fn redimensionar(&mut self, nova_largura: u32, nova_altura: u32) {
        self.largura = nova_largura;
        self.altura = nova_altura;
    }
}

fn main() {
    let mut retangulo = Rectangle {
        largura: 30,
        altura: 50,
    };

    println!(
        "A área do retângulo é {} pixels quadrados.",
        retangulo.calcular_area()
    );

    retangulo.redimensionar(60, 60);

    println!(
        "A área do retângulo é {} pixels quadrados.",
        retangulo.calcular_area()
    );
}