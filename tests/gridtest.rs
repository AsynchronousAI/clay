
use std::io;

fn main() {
    println!("Enter your grid size: ");
    let mut name = String::new();
    io::stdin().read_line(&mut name).expect("Failed to read line");

    // convert string to int
    let name: i32 = name.trim().parse().expect("Please type a number!");

    for i in 1..name+1 {
        for j in 1..name+1 {
            print!("{} ", i * j);
        }
        println!("");
    }
}