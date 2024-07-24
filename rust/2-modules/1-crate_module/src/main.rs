mod file_manager; 
use file_manager::text_file::{create_file, read_file};

fn main() {
    create_file().expect("Error creating file");
    read_file().expect("Error reading file");
}