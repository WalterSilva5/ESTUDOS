use std::io::stdin;

fn main(){
    let mut name = String::new();
    println!("Digite seu nome: ");
    stdin().read_line(&mut name).expect("Falha ao ler o nome");
    name = name.trim().to_string();
    if name.len() > 3 {
        println!("{} tem mais de 3 letras", name);
        println!("len: {}", name.len());
    } else {
        println!("{} tem menos de 3 letras", name);
    }

    let mut age = String::new();
    println!("Digite sua idade: ");
    stdin().read_line(&mut age).expect("Falha ao ler a idade");
    let age: i32 = age.trim().parse().expect("Falha ao converter a idade");
    match age {
        0..=17 => println!("Você é menor de idade"),
        18..=100 => println!("Você é maior de idade"),
        _ => println!("Idade inválida")
    }

    let text_1 = String::from("Hello");
    let text_2 = String::from("World");
    let text_3 = join_strings(text_1, text_2);
    println!("join strings result {}", text_3);
}


fn join_strings(text_1: String, text_2: String) -> String {
    return format!("{} - {}", text_1, text_2);
}