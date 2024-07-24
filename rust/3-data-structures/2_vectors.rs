fn main() {
    // Create an empty vector
    let mut numbers: Vec<i32> = Vec::new();

    // Add elements to the vector
    numbers.push(1);
    numbers.push(2);
    numbers.push(3);

    // Access elements in the vector
    println!("First element: {}", numbers[0]);
    println!("Second element: {}", numbers[1]);

    // Iterate over the vector
    for number in &numbers {
        println!("Number: {}", number);
    }

    // Update an element in the vector
    numbers[0] = 10;

    // Remove an element from the vector
    let removed_number = numbers.pop();

    // Check if the vector is empty
    if numbers.is_empty() {
        println!("The vector is empty");
    } else {
        println!("The vector is not empty");
    }

    // Print the vector
    println!("Vector: {:?}", numbers);
}