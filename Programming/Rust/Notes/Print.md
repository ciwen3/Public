
# Formatted print
## println!
```rust
	println!("Some Text Here");
```
 - println! calls a Rust Macro to print text to the screen
 - println (without the !) calls a normal function 
Examples:
```rust
    println!("You guessed: {guess}");
    println!("x = {x} and y + 2 = {}", y + 2);
```
Printing is handled by a series of macros defined in std::fmt some of which include:
 - format!: write formatted text to String
 - print!: same as format! but the text is printed to the console (io::stdout).
 - println!: same as print! but a newline is appended.
 - eprint!: same as print! but the text is printed to the standard error (io::stderr).
 - eprintln!: same as eprint! but a newline is appended.
