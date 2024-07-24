enum Direction {
    Up,
    Down,
    Left,
    Right,
}

fn main() {
    let player_direction = Direction::Up;

    match player_direction {
        Direction::Up => println!("Moving up!"),
        Direction::Down => println!("Moving down!"),
        Direction::Left => println!("Moving left!"),
        Direction::Right => println!("Moving right!"),
    }
}