
# loop
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
