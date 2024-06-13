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
