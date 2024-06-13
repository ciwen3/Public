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

## Compile Rust Code
```bash
rustc main.rs
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





## prelude: import library
```rust
use std::io;
```
 - To obtain user input and then print the result as output, we need to bring the io input/output library into scope. The io library comes from the standard library, known as std:

## variables
```rust
    let mut guess = String::new();
```
 - let statement to create the variable.
 -  variables are immutable by default, meaning once we give the variable a value, the value won’t change. 
 - The :: syntax in the ::new line indicates that new is an associated function of the String type. An associated function is a function that’s implemented on a type, in this case String. This new function creates a new, empty string. You’ll find a new function on many types because it’s a common name for a function that makes a new value of some kind.
 ```rust
let apples = 5; // immutable: object whose state CANNOT be modified after it is created; unchangeable
let mut bananas = 5; // mutable: object whose state CAN be modified after it is created; changeable
 ```

## constants
```
const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
```
 - values that are bound to a name and are not allowed to change
 - You declare constants using the ```const``` keyword instead of the ```let``` keyword, and the type of the value must be annotated
 - naming convention for constants is to use all uppercase with underscores between words ```THREE_HOURS_IN_SECONDS```

## shadowing
```
fn main() {
    let x = 5;

    let x = x + 1;

    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {x}");
    }

    println!("The value of x is: {x}");
}
```
 - declare a new variable with the same name as a previous variable

```
    let spaces = "   ";
    let spaces = spaces.len();
```
 - The first spaces variable is a string type and the second spaces variable is a number type. Shadowing thus spares us from having to come up with different names, such as spaces_str and spaces_num; instead, we can reuse the simpler spaces name. However, if we try to use mut for this, as shown here, we’ll get a compile-time error:
```
    let mut spaces = "   ";
    spaces = spaces.len();
```

## data types
### scalar types
A scalar type represents a single value. Rust has four primary scalar types: integers, floating-point numbers, Booleans, and characters

### integer types
 - type declaration indicates that the value it’s associated with should be an unsigned integer (signed integer types start with i instead of u) that takes up 32 bits of space. 

| Length | Signed | Unsigned |
|--------|--------|----------|
| 8-bit  | i8     | u8       |
| 16-bit | i16    | u16      |
| 32-bit | i32    | u32      |
| 64-bit | i64    | u64      |
| 128-bit| i128   | u128     |
| arch   | isize  | usize    |

 - isize and usize types depend on the architecture of the computer your program is running on, which is denoted in the table as “arch”: 64 bits if you’re on a 64-bit architecture and 32 bits if you’re on a 32-bit architecture.
 - unsigned: will only ever be positive and can therefore be represented without a sign
 - signed: possible for the number to be negative—in other words, whether the number needs to have a sign with it (plus sign or a minus sign)

| Number literals | Example |
|-----------------|---------|
| Decimal | 98_222 |
| Hex | 0xff |
| Octal | 0o77 |
| Binary | 0b1111_0000 |
| Byte (u8 only) | b'A' |

- Note that number literals that can be multiple numeric types allow a type suffix, such as 57u8, to designate the type. Number literals can also use _ as a visual separator to make the number easier to read, such as 1_000, which will have the same value as if you had specified 1000.

### floating-point types
floating-point numbers are numbers with decimal points
```
fn main() {
    let x = 2.0; // f64

    let y: f32 = 3.0; // f32
}
```
 - f32 32 bits in size
 - f64 64 bits in size
 - default type is f64 because on modern CPUs, it’s roughly the same speed as f32 but is capable of more precision
 - all floating-point types are signed

### numeric operations types
```
fn main() {
    // addition
    let sum = 5 + 10;

    // subtraction
    let difference = 95.5 - 4.3;

    // multiplication
    let product = 4 * 30;

    // division
    let quotient = 56.7 / 32.2;
    let truncated = -5 / 3; // Results in -1

    // remainder
    let remainder = 43 % 5;
}
```
 - supports the basic mathematical operations you’d expect for all the number types: addition, subtraction, multiplication, division, and remainder
 - integer division truncates toward zero to the nearest integer

### boolean types
```
fn main() {
    let t = true;

    let f: bool = false; // with explicit type annotation
}
```

### character types
```
fn main() {
    let c = 'z';
    let z: char = 'ℤ'; // with explicit type annotation
    let heart_eyed_cat = '😻';
}
```
 - Note that we specify char literals with single quotes, as opposed to string literals, which use double quotes
 - ```char``` type is four bytes in size and represents a Unicode Scalar Value, which means it can represent a lot more than just ASCII

## Compound Types
Compound types can group multiple values into one type. Rust has two primitive compound types: tuples and arrays.

### tuple type
tuple is a general way of grouping together a number of values with a variety of types into one compound type. 
```
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
}
```
 - have a fixed length: once declared, they cannot grow or shrink in size
 - create a tuple by writing a comma-separated list of values inside parentheses
 - each position in the tuple has a type, and the types of the different values in the tuple don’t have to be the same
```
fn main() {
    let tup = (500, 6.4, 1);

    let (x, y, z) = tup;

    println!("The value of y is: {y}");
}
```


```
fn main() {
    let x: (i32, f64, u8) = (500, 6.4, 1);

    let five_hundred = x.0;

    let six_point_four = x.1;

    let one = x.2;
}
```

### array type
```
fn main() {
    let a = [1, 2, 3, 4, 5];
}
```
 - every element of an array must have the same type 
 - unlike arrays in some other languages, arrays in Rust have a fixed length.
```
let months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"];
```

```
let a: [i32; 5] = [1, 2, 3, 4, 5];
```
 - write an array’s type using square brackets with the type of each element, a semicolon, and then the number of elements in the array
 - i32 is the type of each element. After the semicolon, the number 5 indicates the array contains five elements

```
let a = [3; 5];
```
 - array named a will contain 5 elements that will all be set to the value 3 initially
 - this is the same as writing let a = [3, 3, 3, 3, 3]; but in a more concise way

```
fn main() {
    let a = [1, 2, 3, 4, 5];

    let first = a[0];
    let second = a[1];
}
```
 - variable named ```first``` will get the value 1 because that is the value at index [0] in the array
 - variable named ```second``` will get the value 2 from index [1] in the array


## functions
```
fn main() {
    println!("Hello, world!");

    another_function();
}

fn another_function() {
    println!("Another function.");
}
```
 - ```fn``` keyword allows you to declare new functions
 - ```fn``` followed by a function name and a set of parentheses. The curly brackets tell the compiler where the function body begins and ends

### parameters/arguments
```
fn main() {
    another_function(5);
}

fn another_function(x: i32) {
    println!("The value of x is: {x}");
}
```
 - are special variables that are part of a function’s signature 
 - when a function has parameters, you can provide it with concrete values for those parameters
 - The declaration of another_function has one parameter named x
 - The type of x is specified as i32
 - When we pass 5 in to another_function, the println! macro puts 5 where the pair of curly brackets containing x was in the format string
 - in function signatures, you must declare the type of each parameter

```
fn main() {
    print_labeled_measurement(5, 'h');
}

fn print_labeled_measurement(value: i32, unit_label: char) {
    println!("The measurement is: {value}{unit_label}");
}
```

### statements 
 - function bodies are made up of a series of statements optionally ending in an expression
 - statements are instructions that perform some action and do not return a value
 - expressions evaluate to a resultant value. Let’s look at some examples
```
fn main() {
    let y = 6;
}
```
 - creating a variable and assigning a value to it with the let keyword is a statement
 - function definitions are also statements
 - statements do not return values

### expressions
 - ***if you add a semicolon to the end of an expression, you turn it into a statement, and it will then not return a value***
 - expressions evaluate to a value 
 - ```let y = 6;``` is an expression that evaluates to the value 6 
 - calling a function is an expression
 - calling a macro is an expression
 - a new scope block created with curly brackets is an expression

```
{
    let x = 3;
    x + 1
}
```
 - in this case, evaluates to 4
 - that value gets bound to y as part of the let statement
 - note that the x + 1 line doesn’t have a semicolon at the end
 - if you add a semicolon to the end of an expression, you turn it into a statement, and it will then not return a value

### functions with return values
```
fn five() -> i32 {
    5
}

fn main() {
    let x = five();

    println!("The value of x is: {x}");
}
```
 - functions can return values to the code that calls them
 - we don’t name return values, but we must declare their type after an arrow (->)
 - the return value of the function is synonymous with the value of the final expression in the block of the body of a function
 - can return early from a function by using the ```return``` keyword and specifying a value, but most functions return the last expression implicitly



```
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1
}
```
 1. x is equal to the return value of plus_one after being run with the parameter/argument 5
 2. function plus_one declares the parameter/arguement as variable x and that it is a signed 32bit integer
 3. print the line with the returned value of x

## if expression

```
fn main() {
    let number = 3;

    if number < 5 {
        println!("condition was true");
    } else {
        println!("condition was false");
    }
}
```


```
fn main() {
    let number = 6;

    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else if number % 2 == 0 {
        println!("number is divisible by 2");
    } else {
        println!("number is not divisible by 4, 3, or 2");
    }
}
```

### using if in a let statement
```
fn main() {
    let condition = true;
    let number = if condition { 5 } else { 6 };

    println!("The value of number is: {number}");
}
```
 - ```number``` variable will be bound to a value based on the outcome of the ```if``` expression
 - results from each arm of the ```if``` must be the same type

## loop
```
loop {}
```
 - will rerun the code between the {} forever or until there is an exit condition

 ```
fn main() {
    loop {
        println!("again!");
    }
}
 ```

### returning values from loops
```
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    println!("The result is {result}");
}
```
- you can add the value you want returned after the break expression you use to stop the loop; that value will be returned out of the loop so you can use it

### loop labels to disambiguate between multiple loops
If you have loops within loops, break and continue apply to the innermost loop at that point. You can optionally specify a loop label on a loop that you can then use with break or continue to specify that those keywords apply to the labeled loop instead of the innermost loop. Loop labels must begin with a single quote.
```
fn main() {
    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }

        count += 1;
    }
    println!("End count = {count}");
}
```
 - the outer loop has the label 'counting_up, and it will count up from 0 to 2
 - the inner loop without a label counts down from 10 to 9
 - the first break that doesn’t specify a label will exit the inner loop only
 - the break 'counting_up; statement will exit the outer loop

### conditional loops with while
A program will often need to evaluate a condition within a loop. While the condition is true, the loop runs. When the condition ceases to be true, the program calls break, stopping the loop. It’s possible to implement behavior like this using a combination of loop, if, else, and break. However, this pattern is so common that Rust has a built-in language construct for it, called a while loop. This construct eliminates a lot of nesting that would be necessary if you used loop, if, else, and break, and it’s clearer. 

```
fn main() {
    let mut number = 3;

    while number != 0 {
        println!("{number}!");

        number -= 1;
    }

    println!("LIFTOFF!!!");
}
```
 - while a condition evaluates to true, the code runs; otherwise, it exits the loop

### looping through a collection with for

```
fn main() {
    let a = [10, 20, 30, 40, 50];
    let mut index = 0;

    while index < 5 {
        println!("the value is: {}", a[index]);

        index += 1;
    }
}
```
 - use the while construct to loop over the elements of a collection, such as an array

```
fn main() {
    let a = [10, 20, 30, 40, 50];

    for element in a {
        println!("the value is: {element}");
    }
}
```
 - less error prone than the example above it 

```
fn main() {
    for number in (1..4).rev() {
        println!("{number}!");
    }
    println!("LIFTOFF!!!");
}
```
 - ```rev``` to reverse the range

## break
```
break;
```
 - makes the program exit the loop

## user input
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

## convert variable type
```
let guess: u32 = guess.trim().parse().expect("Please type a number!");
```
Rust allows us to shadow the previous value of guess with a new one. Shadowing lets us reuse the guess variable name rather than forcing us to create two unique variables

 - ```trim()``` method on a String instance will eliminate any whitespace at the beginning and end
 - ```parse()``` method on strings converts a string to another type
 - ```let guess: u32``` The colon (:) after guess tells Rust we’ll annotate the variable’s type

## continue
```
let guess: u32 = match guess.trim().parse() {
	Ok(num) => num,
	Err(_) => continue,
};
```
 - ```continue``` which tells the program to go to the next iteration of the loop 
 - in this example it asks for another guess when an error like a non integer is input occurs 

## catch all
```
Err(_)
```
 - ```_``` is a catchall value; in this example, we’re saying we want to match all Err values, no matter what information they have inside them





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

The program will generate a file main.exe once compiled. Multiple command line parameters should be separated by space. Execute main.exe from the terminal as main.exe hello tutorialspoint.

NOTE − hello and tutorialspoint are commandline arguments.

Output:
```
No of elements in arguments is :3
[main.exe]
[hello]
[tutorialspoint]
```
The output shows 3 arguments as the main.exe is the first argument.




# Math
The following program calculates the sum of values passed as commandline arguments. A list integer values separated by space is passed to program.
```rust
fn main(){
   let cmd_line = std::env::args();
   println!("No of elements in arguments is 
   :{}",cmd_line.len()); 
   // total number of elements passed

   let mut sum = 0;
   let mut has_read_first_arg = false;

   //iterate through all the arguments and calculate their sum

   for arg in cmd_line {
      if has_read_first_arg { //skip the first argument since it is the exe file name
         sum += arg.parse::<i32>().unwrap();
      }
      has_read_first_arg = true; 
      // set the flag to true to calculate sum for the subsequent arguments.
   }
   println!("sum is {}",sum);
}
```

On executing the program as main.exe 1 2 3 4, the output will be −
```
No of elements in arguments is :5
sum is 10
```




# Issuing commands
https://fitech101.aalto.fi/programming-languages/rust/8-interaction-input-and-os/
