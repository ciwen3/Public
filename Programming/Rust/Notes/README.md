# Rust
 - https://www.rust-lang.org/learn
 - https://doc.rust-lang.org/rust-by-example/
 - https://www.youtube.com/watch?v=RU7BYxmSBNg
 - https://rust-classes.com/
 - https://www.tutorialspoint.com/rust/index.htm

## Writing Linux Kernel Modules in Rust
 - https://www.linuxfoundation.org/webinars/writing-linux-kernel-modules-in-rust
 - https://www.sobyte.net/post/2022-11/rust-kernel/
 - https://www.jackos.io/rust-kernel/rust-for-linux.html
 - https://www.youtube.com/watch?v=tPs1uRqOnlk
 - https://www.youtube.com/watch?v=RyY01fRyGhM

## Manually Compile Rust Code
```bash
rustc main.rs
```

## Compile with Cargo
just bulild and test the code is not breaking any Rust rules. 
```bash
cargo build
```
OR bulild and test the code is not breaking any Rust rules and then run the compiled program. 
```bash
cargo run
```

# Anatomy of a Rust Program
## main function
https://doc.rust-lang.org/book/ch01-02-hello-world.html
```rust
fn main() {

}
```
 - The fn syntax declares a new function; the parentheses, (), indicate there are no parameters; and the curly bracket, {, starts the body of the function.
 - () Parameters goes inside the parentheses
 - {} Function body goes inside the curly brackets. Rust requires curly brackets around all function bodies. 

## comment
```rust
// everything after a double slash is ignored by the compiler
```

## prelude: import library
```rust
use std::io;
```
 - To obtain user input and then print the result as output, we need to bring the io input/output library into scope. The io library comes from the standard library, known as std:



