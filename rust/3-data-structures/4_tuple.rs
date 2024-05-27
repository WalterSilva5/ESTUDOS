fn main() {
    // Creating a tuple
    let person = ("John", 25, true);

    // Accessing tuple elements
    let name = person.0;
    let age = person.1;
    let is_employed = person.2;

    // Printing tuple elements
    println!("Name: {}", name);
    println!("Age: {}", age);
    println!("Is Employed: {}", is_employed);
}