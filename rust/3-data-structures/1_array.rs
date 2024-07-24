fn main() {
    let numbers: [i32; 5] = [1, 2, 3, 4, 5];

    println!("First element: {}", numbers[0]);
    println!("Second element: {}", numbers[1]);

    let mut names: [String; 3] = ["Alice".to_string(), "Bob".to_string(), "Charlie".to_string()];
    names[2] = "David".to_string();

    for number in numbers.iter() {
        println!("Number: {}", number);
    }

    println!("Array length: {}", numbers.len());
}