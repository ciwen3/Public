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

