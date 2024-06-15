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





## Example #3
To issue a command using the operating system's terminal in Rust, you can use the `std::process::Command` module. Here's a basic example of how you can execute a command from a Rust program:

```rust
use std::process::Command;

fn main() {
    // Command to execute (example: list files in current directory)
    let command = "ls";

    // Execute the command
    let output = Command::new(command)
        .output()
        .expect("Failed to execute command");

    // Check if the command was successful
    if output.status.success() {
        // Convert the output to a string (assuming UTF-8)
        let stdout = String::from_utf8_lossy(&output.stdout);
        println!("Command output:\n{}", stdout);
    } else {
        // Print any error messages
        let stderr = String::from_utf8_lossy(&output.stderr);
        eprintln!("Error executing command: {}", stderr);
    }
}
```

### Explanation:

1. **Importing `Command`**: `use std::process::Command;` brings the `Command` struct into scope, which allows you to construct and execute commands.
2. **Defining the Command**: `let command = "ls";` specifies the command you want to execute. Replace `"ls"` with any command you would like to run.
3. **Executing the Command**: `Command::new(command)` creates a new command instance. Additional methods like `.arg("argument")` can be chained to specify command-line arguments if needed.
4. **Handling Output**: `.output()` method executes the command and waits for it to complete. It returns a `std::process::Output` struct.
5. **Checking Success**: `output.status.success()` checks if the command was executed successfully.
6. **Accessing Output**: `output.stdout` and `output.stderr` contain the standard output and standard error streams of the command, respectively. They are returned as `Vec<u8>` buffers, which you can convert to strings using `String::from_utf8_lossy()`.
7. **Printing Results**: Depending on whether the command succeeded or failed, you can print the output or error messages accordingly.

### Additional Notes:
- Make sure to handle errors properly, as shown in the example (`expect` and checking `success()`).
- Depending on your operating system and the command you want to execute, you may need to adjust the command syntax and arguments.
- For more complex scenarios, such as streaming input to a process or handling interactive commands, Rust provides additional capabilities in its `process` module.

This example demonstrates the basic framework for executing commands within a Rust program and capturing their output. Adjustments can be made based on specific requirements or additional functionality needed.






## Example #4
The code provided in the previous response is designed to work on Unix-like systems (such as Linux and macOS). However, to ensure cross-platform compatibility, especially with Windows, you need to make a few adjustments:

### Cross-Platform Considerations:

1. **Command Separators**:
   - On Unix-like systems (Linux, macOS), the command separator in the shell is typically a space (`ls -l`).
   - On Windows, the command separator is `cmd.exe /C` before the command (`cmd.exe /C dir`).

2. **Path Separators**:
   - Unix-like systems use forward slashes (`/`) for paths (`/home/user/file.txt`).
   - Windows uses backslashes (`\`) for paths (`C:\Users\User\File.txt`).

3. **Environment Variables**:
   - Environment variable access is different (`$HOME` on Unix-like vs `%USERPROFILE%` on Windows).

### Adjusted Example for Cross-Platform Compatibility:

Here's how you can adjust the example to work on both Linux and Windows:

```rust
use std::process::Command;

fn main() {
    // Define the command based on the current platform
    let (command, args) = if cfg!(target_os = "windows") {
        ("cmd.exe", ["/C", "dir"])
    } else {
        ("ls", [])
    };

    // Execute the command
    let output = Command::new(command)
        .args(&args)
        .output()
        .expect("Failed to execute command");

    // Check if the command was successful
    if output.status.success() {
        // Convert the output to a string (assuming UTF-8)
        let stdout = String::from_utf8_lossy(&output.stdout);
        println!("Command output:\n{}", stdout);
    } else {
        // Print any error messages
        let stderr = String::from_utf8_lossy(&output.stderr);
        eprintln!("Error executing command: {}", stderr);
    }
}
```

### Explanation of Adjustments:

- **Platform Detection**: `cfg!(target_os = "windows")` is used to check if the target platform is Windows. This allows you to choose different commands and arguments based on the operating system.

- **Command and Arguments**: 
  - On Windows, `cmd.exe` is used as the command, with `"/C"` and `"dir"` as arguments (`/C` indicates that `cmd.exe` should run the command and then terminate).
  - On Unix-like systems (Linux), `"ls"` is used as the command with an empty array `[]` for arguments, as `ls` doesn't typically need arguments for basic usage.

- **Handling Output**: The rest of the code remains the same as in the previous example, ensuring that you capture and handle the output and errors appropriately for both platforms.

By making these adjustments, the Rust code can now execute basic commands (`dir` on Windows and `ls` on Unix-like systems) on both Windows and Linux. For more complex commands or specific requirements, further adjustments may be necessary, but this serves as a good starting point for cross-platform command execution in Rust.




### Reference:
https://fitech101.aalto.fi/programming-languages/rust/8-interaction-input-and-os/
