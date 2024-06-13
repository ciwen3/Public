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
