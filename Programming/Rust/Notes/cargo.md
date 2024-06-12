## Cargo 
https://doc.rust-lang.org/book/ch01-03-hello-cargo.html




https://Crates.io - Crates.io is where people in the Rust ecosystem post their open source Rust projects for others to use.

1. show version of cargo installed
```rust
cargo --version
```

2. create new project using cargo
```rust
cargo new {project name}
```
 - creates new folder with {project name}. This top-level project directory is just for README files, license information, configuration files, and anything else not related to your code.
 - creates Cargo.toml file in Project folder
 - creates new folder in Project folder called src
 - creates main.rs file in src folder. Cargo expects your source files to live inside the src directory.
 - Note: You can change cargo new to use a different version control system or no version control system by using the --vcs flag. ```cargo new --vcs=git ```

3. build a project using cargo
```rust
cargo build
```
 - creates an executable file in target/debug/hello_cargo (or target\debug\hello_cargo.exe on Windows) rather than in your current directory. Because the default build is a debug build, Cargo puts the binary in a directory named debug. 
 - Running cargo build for the first time also causes Cargo to create a new file at the top level: Cargo.lock. This file keeps track of the exact versions of dependencies in your project. 

4. build and run a progam in one step
```rust
cargo run
```
5. build a project without producing a binary to check for errors 
```rust
cargo check
```
6. compile it with optimizations
```rust
cargo build --release
```
 - create an executable in target/release instead of target/debug. The optimizations make your Rust code run faster, but turning them on lengthens the time it takes for your program to compile.
 - If you’re benchmarking your code’s running time, be sure to run ```cargo build --release``` and benchmark with the executable in target/release.

7. build documentation provided by all your dependencies locally and open it in your browser. 
```rust
cargo doc --open
```

8. Updating a Crate to Get a New Version
```
cargo update
```
 - will ignore the Cargo.lock file and figure out all the latest versions that fit your specifications in Cargo.toml
 - will then write those versions to the Cargo.lock file
 

## Cargo.toml
```
[package]
name = "hello_cargo"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
```
 - This file is in the TOML (Tom’s Obvious, Minimal Language) format, which is Cargo’s configuration format.
 - [package], is a section heading that indicates that the following statements are configuring a package.
 - [dependencies], is the start of a section for you to list any of your project’s dependencies.

 ### depenencies
 ```
[dependencies]
rand = "0.8.5"
```
  -  Cargo understands Semantic Versioning (sometimes called SemVer), which is a standard for writing version numbers. The specifier 0.8.5 is actually shorthand for ^0.8.5, which means any version that is at least 0.8.5 but below 0.9.0.

## Cargo.lock 
Cargo has a mechanism that ensures you can rebuild the same artifact every time you or anyone else builds your code: Cargo will use only the versions of the dependencies you specified until you indicate otherwise. For example, say that next week version 0.8.6 of the rand crate comes out, and that version contains an important bug fix, but it also contains a regression that will break your code. To handle this, Rust creates the Cargo.lock file the first time you run cargo build, so we now have this in the guessing_game directory.

When you build a project for the first time, Cargo figures out all the versions of the dependencies that fit the criteria and then writes them to the Cargo.lock file. When you build your project in the future, Cargo will see that the Cargo.lock file exists and will use the versions specified there rather than doing all the work of figuring out versions again. This lets you have a reproducible build automatically. In other words, your project will remain at 0.8.5 until you explicitly upgrade, thanks to the Cargo.lock file. Because the Cargo.lock file is important for reproducible builds, it’s often checked into source control with the rest of the code in your project.



