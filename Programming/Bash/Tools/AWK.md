# AWK variables:
```
$0 for the whole line.
$1 for the first field.
$2 for the second field.
$n for the nth field.
```

# AWK (print): equivalent to cat filename
### print file contents:
```
awk '{print $0}' filename
```

### print 1st & 4th column:
```
awk '{print $1, $4}' filename
```

### concatenate 1st & 4th column:
```
awk '{print $1.$4}' filename
```

### print second column if the first column contains a #:
```
awk '$1 == "#" {print $2}' filenmae
```

### if # is found anywhere on the line print that line:
```
awk '$1 ~ "#" {print $2}' filename
```

### if # is NOT found anywhere on the line print that line:
```
awk '$1 !~ "#" {print $2}' filename
```

### print specific lines of the file: equivalent to head filename
```
awk '(NR>=0 && NR<=11){print} (NR==11){exit}' filename
```

### case insensitive search print lines with dir:
```
awk 'tolower($0) ~ /dir/' filename
```

### Print every line that has "test" in it:
```
awk '/test/ { print }' filename
```

### Print every line that has a number in it:
```
awk '/[0-9]/ { print }' filename
```

### Print every line that starts with a number:
```
awk '/^[0-9]/ { print }' filename
```

### Print every line that ends with a number:
```
awk '/[0-9]$/ { print }' filename
```

### print if first line starts with "123":
```
awk '{ if($1 ~ /123) print }' filename
```

### replace string: equivalent to sed
```
awk '{ gsub("string to remove","string to input"); print $0}' /path/to/file > /path/to/save/file
```

### remove string: equivalent to sed
```
awk '{ gsub("string to remove",""); print $0}' /path/to/file > /path/to/save/file
```


### strip /etc/shadow of everything but the username and password hash
```
sudo awk -F : '$2 ~ /\$/ {print $1 ":" $2}' /etc/shadow > /tmp/shadow

sudo awk -F : '$2 ~ /\$/ { gsub("\$"," "); print $1 ":" $2}' /etc/shadow > /tmp/shadow
```



### Remove the first character of everyline: 
```
awk '{print substr($0,2,length()-1);}' input.txt > output.txt
```



# AWK replace other tools

### cat filename:
```
awk '{print $0}' filename
```

### grep '#' filename:
```
awk '/#/' filename
```

### head filename:
```
awk '{print $0} (NR==11){exit}' filename 
```

### tail filename:
```
awk '{ array[NR]=$0 } END { for (i=NR-10; i<=NR; i++) print array[i] }' filename 
```

### sed s/"string to remove"/"string to input"/g > /path/to/save/filename
```
awk '{ gsub("string to remove","string to input"); print $0}' /path/to/filename > /path/to/save/filename
```

### sed s/"string to remove"/""/g > /path/to/save/filename
```
awk '{ gsub("string to remove",""); print $0}' /path/to/filename > /path/to/save/filename
```

### for loop to rename all mp4 files to just the first 11 characters (1, 11) 
```bash
for i in $(ls *.mp4); do mv $i $(echo $i | awk '{print substr($i, 1, 11)}').mp4 ; done
```
1. https://www.gnu.org/software/gawk/manual/html_node/String-Functions.html
2. https://thomas-cokelaer.info/blog/2011/05/awk-the-substr-command-to-select-a-substring/
