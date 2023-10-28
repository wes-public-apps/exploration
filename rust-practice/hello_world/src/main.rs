// single line comment
/* Block comments that end by the closing delimeter */

// this is the entrypoint functions for rust
fn main() {
    println!("Hello, world!");

    // empty {} will be replaced with corresponding ordered variable list
    println!("{} Hello, World {}", "item1", "item2");
    // item1 Hello, World item2

    // numbered brackets (ie {0}) will be replaced with corresponding variable index
    println!("{0} Hello, World {0}", "--------------");
    // -------------- Hello, World --------------
    println!("{0}, this is {1}. {1}, this is {0}", "Alice", "Bob");
    // Alice, this is Bob. Bob, this is Alice

    // named variables are supported
    println!(
        "{subject} {verb} {object}",
        object = "the lazy dog",
        subject = "the quick brown fox",
        verb = "jumps over"
    );
    // the quick brown fox jumps over the lazy dog

    // specify the format character
    println!("Base 10               {}", 69420); // 69420
    println!("Base 2                {:b}", 69420); // 10000111100101100
    println!("Base 8                {:o}", 69420); // 207454
    println!("Base 16               {:x}", 69420); // 10f2c
    println!("Base 16 Capital       {:X}", 69420); // 10F2C

    // right justify
    println!("{0:>5}", 1);
    //     1

    // pad numbers with 0
    println!("{0:0>5}", 1);
    //00001
    // flip and left justify
    println!("{0:0<5}", 1)
    //10000
}
