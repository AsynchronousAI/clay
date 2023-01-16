fn main(){
    // print a multiplication table with 10 rows and 10 columns and all of the numbers are aligned to the right
    for i in 1..20{
        for j in 1..20{
            print!("{:>4}", i*j);
        }
        println!();
    }
}