# functions
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

## parameters/arguments
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

## statements 
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

## expressions
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

## functions with return values
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
