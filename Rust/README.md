https://www.rust-lang.org/learn/get-started

# Cargo: the Rust build tool and package manager
## Install
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
When you install Rustup you’ll also get the latest stable version of the Rust build tool and package manager, also known as Cargo. Cargo does lots of things:

build your project with 
```
cargo build
```

run your project with 
```
cargo run
```

test your project with 
```
cargo test
```

build documentation for your project with 
```
cargo doc
```

publish a library to crates.io with 
```
cargo publish
```









# Generating a new project
Let’s write a small application with our new Rust development environment. To start, we’ll use Cargo to make a new project for us. In your terminal of choice run:
```
cargo new hello-rust
```
This will generate a new directory called hello-rust with the following files:
```
hello-rust
|- Cargo.toml
|- src
  |- main.rs
```
Cargo.toml is the manifest file for Rust. It’s where you keep metadata for your project, as well as dependencies.

src/main.rs is where we’ll write our application code.

cargo new generates a "Hello, world!" project for us! We can run this program by moving into the new directory that we made and running this in our terminal:
```
cargo run
```
You should see this in your terminal:
```
$ cargo run
   Compiling hello-rust v0.1.0 (/Users/ag_dubs/rust/hello-rust)
    Finished dev [unoptimized + debuginfo] target(s) in 1.34s
     Running `target/debug/hello-rust`
Hello, world!
```

# Adding dependencies
Let’s add a dependency to our application. You can find all sorts of libraries on crates.io, the package registry for Rust. In Rust, we often refer to packages as “crates.”

In this project, we’ll use a crate called ferris-says.

In our Cargo.toml file we’ll add this information (that we got from the crate page):
```
[dependencies]
ferris-says = "0.3.1"
```

We can also do this by running 
```
cargo add ferris-says.
```

Now we can run:
```
cargo build
```
...and Cargo will install our dependency for us.

You’ll see that running this command created a new file for us, Cargo.lock. This file is a log of the exact versions of the dependencies we are using locally.

To use this dependency, we can open main.rs, remove everything that’s in there (it’s just another example), and add this line to it:
```
use ferris_says::say;
```

This line means that we can now use the say function that the ferris-says crate exports for us.

A small Rust application
Now let’s write a small application with our new dependency. In our main.rs, add the following code:
```
use ferris_says::say; // from the previous step
use std::io::{stdout, BufWriter};

fn main() {
    let stdout = stdout();
    let message = String::from("Hello fellow Rustaceans!");
    let width = message.chars().count();

    let mut writer = BufWriter::new(stdout.lock());
    say(&message, width, &mut writer).unwrap();
}
```
Once we save that, we can run our application by typing:
```
cargo run
```
Assuming everything went well, you should see your application print this to the screen:
```
 __________________________
< Hello fellow Rustaceans! >
 --------------------------
        \
         \
            _~^~^~_
        \) /  o o  \ (/
          '_   -   _'
          / '-----' \
```

To test that you have Rust and Cargo installed, you can run this in your terminal of choice:
```
cargo --version
```
