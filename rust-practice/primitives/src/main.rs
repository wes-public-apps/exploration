// The goal of this tutorial is to learn about Rust primitives

fn main() {
    let logical: bool = true;

    let a_float: f64 = 1.0; // regular annotation
    let an_integer = 5i32; // suffix annotation

    // direct type inferrence
    let default_float = 3.0; // f64
    let default_integer = 7; // i32

    // indirect type inference
    let mut inferred_type = 12; // i64
    inferred_type = 438905438732339i64;

    // mutable variables (value can be changed)
    let mut mutable = 12; // i32 variable that can change
    mutable = 12;

    // Type error is caught here
    mutable = true;

    // shadowing - Variables can be overwritten
    let mutable = true;

    println!("Variable tutorial");
}
