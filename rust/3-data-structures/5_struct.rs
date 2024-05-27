// Define a struct named `Person`
struct Person {
    name: String,
    age: u32,
}

fn main() {
    // Create a new instance of `Person`
    let person = Person {
        name: String::from("John Doe"),
        age: 30,
    };

    // Access the fields of the struct
    println!("Name: {}", person.name);
    println!("Age: {}", person.age);
}