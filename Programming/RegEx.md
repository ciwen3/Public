# Regex Practice:
https://regexone.com/


# REGEX:
```
^ symbol: indicate the search pattern should consider a match only if it appears at the start of a line. 
$ symbol: indicate the search pattern should consider a match only if it appears at the end of a line.
[]: should consider a match if any character in here matches
a-z: should consider a match if any character matchs the lowercase alphabet
. : wildcard for any single character
.* : wildcard for any character and any length of characters
```



## Examples: 
```
g[eao]t = get gat got
g[a-e]t = gat get 
g.t = g*(any one character)t gat get git got 
g.*t = g*(any character any length)t gat get git got great goat etc...
```







# Regex	Definition	
```
^	Matches the beginning of a line	
$	Matches the end of the line	
.	Matches any character	
\s	Matches whitespace ( , \t, \r, \n)	
\S	Matches any non-whitespace character	
X?	0 or 1 instances of X	
X{m}	exactly m instances of X	
X{m,}	at least m instances of X	
X{m,n}	between m and n (inclusive) instances of X	
X*	Repeats X zero or more times	
X*?	Repeats X zero or more times (non-greedy)	
X+	Repeats X one or more times	
X+?	Repeats X one or more times (non-greedy)	
[aeiou]	Matches a single character in the listed set	
[^XYZ]	Matches a single character not in the listed set	
[a-z0-9]	The set of characters can include a range	
(	Indicates where string extraction is to start	
)	Indicates where string extraction is to end	
\d	digit in 0123456789	
\D	non-digit	
\w	"word" (letters and digits and _)	
\W	non-word	
\t	tab	
\r	return	
\n	new line	
	space	
\b	word boundaries (defined as any edge between a \w and a \W)	\bcat\b finds a match in "the cat in the hat" but not in "locate"
 X | Y	disjunction X or Y	\b(cat|dog)s\b matches cats and dogs
```	


# Special Characters:
```
{} [] () ^ $ . | * + ? \
```

# Usage example	Match any email address from the domains yahoo.com, hotmail.com, and gmail.com.
## Regex example:
```
(\W|^)[\w.\-]{0,25}@(yahoo|hotmail|gmail)\.com(\W|$)
```
# Usage example	Match any IP address within the range 192.168.1.0 to 192.168.1.255.
## Regex examples:	
1.   192\.168\.1\.
2.   192\.168\.1\.\d{1,3}

# Usage example	Match any word or phrase in the following list:
```
baloney
darn
drat
fooey
gosh darnit
heck
```
## Regex example:
```
(?i)(\W|^)(baloney|darn|drat|fooey|gosh\sdarnit|heck)(\W|$)
```

# EMAIL 
## Regex example:
```
/\A[a-z0-9\+\-_\.]+@[a-z\d\-.]+\.[a-z]+\z/i
```
```
/\A[a-zA-Z0-9.!\#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+\z/
```

# web requests
HTTP, HTTPS, FTP, IPv4
```regex
(((http|https|ftp):\/\/)|((\d{1,3}\.){3}\d{1,3}))
```



# References:
1. https://support.google.com/a/answer/1371417?hl=en#Match-Any-Email-Address-from-a-Spec
2. regex101.com
