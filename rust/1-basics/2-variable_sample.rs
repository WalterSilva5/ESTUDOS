fn main() {
    let var_test = "exemplo variavel";
    let mut number_var_test:i64 = 100_100_100_100;
    const DEFAULT_NUMBER_ADD:i32 = 10;
    let username:&str = "walter";

    let mut empty_string = String::new();

    number_var_test += 5;
    println!("conteudo da variavel: {}", var_test);
    println!("conteudo da variavel numerica: {}", number_var_test);
    println!("conteudo da variavel numerica padrão: {}", DEFAULT_NUMBER_ADD);
    println!("conteudo da variavel nome: {}", username); 
    println!("conteudo da variavel vazia: {}", empty_string);
    empty_string = "teste string vazia".to_string();
    println!("conteudo da variavel vazia modificada: {}", empty_string);
    println!("o tamanho da variavel vazia modificada: {}", empty_string.len());

    let string_with_spaces = "   Ola mundo teste".to_string();
    println!("conteudo da variavel com espacos: {}", string_with_spaces);
    println!("apos remover os espacos: {}", string_with_spaces.trim());
    println!("chars da variavel com espacos: {}", string_with_spaces.chars().count());

    //exibir cada valor da variavel em um for
    for c in string_with_spaces.trim().chars() {
        println!(" char {}", c);
    }

    empty_string.push_str(" teste de concatenacao");
    println!("conteudo da variavel vazia modificada com push: {}", empty_string);
}