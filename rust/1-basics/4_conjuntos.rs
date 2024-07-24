fn main(){
    let sample_touple:(i32, f64, char) = (500, 6.4, 'c');
    println!("touple {} {} {}", sample_touple.0, sample_touple.1, sample_touple.2);

    let sample_array:[i32; 5] = [1, 2, 3, 4, 5];
    println!("array: {} {} {}", sample_array[0], sample_array[1], sample_array[2]);

    //destructuring

    let (var_1, var_2, var_3) = sample_touple;

    println!("destructuring touple: {} {} {}", var_1, var_2, var_3);
}