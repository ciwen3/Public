# CommandLine Arguments
CommandLine arguments are passed to a program before executing it. They are like parameters passed to functions. CommandLine parameters can be used to pass values to the main() function. The std::env::args() returns the commandline arguments.

The following example passes values as commandLine arguments to the main() function. The program is created in a file name main.rs.

```rust
//main.rs
fn main(){
   let cmd_line = std::env::args();
   println!("No of elements in arguments is :{}",cmd_line.len()); 
   //print total number of values passed
   for arg in cmd_line {
      println!("[{}]",arg); //print all values passed 
      as commandline arguments
   }
}
```

The program will generate a file main.exe once compiled. Multiple command line parameters should be separated by space. Execute main.exe from the terminal as 
```bash
main.exe hello tutorialspoint
```
NOTE − hello and tutorialspoint are commandline arguments.

Output:
```
No of elements in arguments is :3
[main.exe]
[hello]
[tutorialspoint]
```
The output shows 3 arguments as the main.exe is the first argument.

## Example #2
```rust
use std::io;

fn main() {
    let mut input = String::new();
    match io::stdin().read_line(&mut input) {
        Ok(n) => {
            println!("{} bytes read", n);
            println!("{}", input);
        }
        Err(error) => println!("error: {error}"),
    }
}

```







### Break Down: 

```rust
use std::io;

fn main() {
    let mut input = String::new();
```
1. `use std::io;`: This line imports the `io` module from the standard library (`std`).
2. `fn main() {`: This declares the main function, which is the entry point of a Rust program.
3. `let mut input = String::new();`: This creates a mutable variable named `input` of type `String` and initializes it with an empty string (`String::new()`). This string will store the input read from the standard input.

```rust
    match io::stdin().read_line(&mut input) {
```
4. `io::stdin()`: This function returns a handle to the standard input stream (`stdin()` from the `io` module).
5. `.read_line(&mut input)`: This method reads a line from the standard input stream and appends it to the `input` string. It takes a mutable reference to `input` (`&mut input`) because it modifies `input` by appending the read line.
6. `match ... { }`: This begins a `match` expression, which is Rust's way of handling control flow based on the result of a pattern match.

```rust
        Ok(n) => {
            println!("{} bytes read", n);
            println!("{}", input);
        }
```
7. `Ok(n) => { ... }`: If the result of `read_line` is `Ok(n)`, where `n` is the number of bytes read (including the newline character), then execute the block inside `{ ... }`.
8. `println!("{} bytes read", n);`: This prints the number of bytes read to the standard output.
9. `println!("{}", input);`: This prints the content of the `input` string (the line read from standard input) to the standard output.

```rust
        Err(error) => println!("error: {error}"),
    }
```
10. `Err(error) => println!("error: {error}"),`: If there's an error during reading, `read_line` returns an `Err` variant with an associated `error`. This block handles that error case by printing an error message. Note the `{error}` placeholder inside the string, which is meant to interpolate the actual error value.

```rust
}
```
11. `}`: Closes the main function.

### Summary:
This Rust program reads a line of input from the standard input, prints the number of bytes read, and then prints the input line itself. If an error occurs during reading, it prints an error message indicating the nature of the error. This is a basic example demonstrating Rust's error handling with `Result` and `match`, along with simple input/output operations using `std::io`.






### Reference:
https://fitech101.aalto.fi/programming-languages/rust/8-interaction-input-and-os/
