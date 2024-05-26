use rand::Rng;

fn main() {
    let mut rng = rand::thread_rng();

    let n: u32 = rng.gen_range(1..=10);
    println!("Número aleatório entre 1 e 10: {}", n);

    let f: f64 = rng.gen();
    println!("Número aleatório de ponto flutuante entre 0 e 1: {}", f);

    let choices = vec!["maçã", "banana", "laranja"];
    let random_choice = choices[rng.gen_range(0..choices.len())];
    println!("Escolha aleatória: {}", random_choice);
}
