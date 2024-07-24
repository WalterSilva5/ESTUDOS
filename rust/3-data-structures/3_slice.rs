fn main() {
    let numbers = [1, 2, 3, 4, 5];
    
    // Creating a slice from the array
    let slice = &numbers[1..4];
    
    // Printing the slice
    println!("Slice: {:?}", slice);
    
    // Modifying the original array through the slice
    slice[0] = 10;
    
    // Printing the modified array
    println!("Modified Array: {:?}", numbers);
}