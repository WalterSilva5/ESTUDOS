// Define a generic function that takes in two arguments of any type
fn print_values<T>(value1: T, value2: T) {
    println!("Value 1: {:?}", value1);
    println!("Value 2: {:?}", value2);
}

fn main() {
    // Call the generic function with different types
    print_values(10, 20); // Prints: Value 1: 10, Value 2: 20
    print_values("Hello", "World"); // Prints: Value 1: "Hello", Value 2: "World"
    print_values(true, false); // Prints: Value 1: true, Value 2: false
}