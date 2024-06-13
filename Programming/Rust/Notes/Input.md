# user input
```rust
    io::stdin()
        .read_line(&mut guess)
```
 - the input/output functionality from the standard library with ```use std::io;```
 - If we hadn’t imported the io library with use std::io; at the beginning of the program, we could still use the function by writing this function call as std::io::stdin. 
 - ```.read_line(&mut guess)``` calls the read_line method on the standard input handle to get input from the user. 
 - passing ```&mut guess``` as the argument to read_line to tell it what string to store the user input in.
 - read_line is to take whatever the user types into standard input and append that into a string 
 - The string argument needs to be mutable so the method can change the string’s content.
 - ```&``` indicates that this argument is a reference, which gives you a way to let multiple parts of your code access one piece of data without needing to copy that data into memory multiple times.
 - references are immutable by default. Hence, you need to write &mut guess rather than &guess to make it mutable. 

## handling potential failure with result
```rust
        .expect("Failed to read line");
```
We could have written this code as:
```rust
io::stdin().read_line(&mut guess).expect("Failed to read line");
```
 - often wise to introduce a newline and other whitespace to help break up long lines when you call a method with the .method_name() syntax. 
 - read_line puts whatever the user enters into the string we pass to it, but it also returns a Result value.
