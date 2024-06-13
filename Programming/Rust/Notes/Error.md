## continue
```
let guess: u32 = match guess.trim().parse() {
	Ok(num) => num,
	Err(_) => continue,
};
```
 - ```continue``` which tells the program to go to the next iteration of the loop 
 - in this example it asks for another guess when an error like a non integer is input occurs 

## catch all
```
Err(_)
```
 - ```_``` is a catchall value; in this example, we’re saying we want to match all Err values, no matter what information they have inside them

## break
```
break;
```
 - makes the program exit the loop
