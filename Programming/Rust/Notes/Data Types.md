# data types
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
