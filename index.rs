mod clayForRust;
fn main(){
    for i in 1..12 {
        for y in 1..12 {
            let len = (i * y).to_string().len();
            let space = 4 - len;
            for _ in 0..space {
                print!(" ");
            }
            print!("{}".concat(space), i * y)
        }
        println!("")
    }
}