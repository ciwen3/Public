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

https://fitech101.aalto.fi/programming-languages/rust/8-interaction-input-and-os/
