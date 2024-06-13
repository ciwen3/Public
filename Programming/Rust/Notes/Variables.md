# variables
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


# constants
```
const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
```
 - values that are bound to a name and are not allowed to change
 - You declare constants using the ```const``` keyword instead of the ```let``` keyword, and the type of the value must be annotated
 - naming convention for constants is to use all uppercase with underscores between words ```THREE_HOURS_IN_SECONDS```


# shadowing
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
