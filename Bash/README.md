# Bedtime Bash Script
![Screenshot](https://img.shields.io/badge/Language-Bash-blue)
![Screenshot](https://img.shields.io/badge/Platform-Linux-brightgreen)

https://github.com/ciwen3/Public/tree/master/Bash/bedtime

used to power down my kids Linux computers at a set time. the files can be installed anywhere so long as your kids don't have sudo access and you use the chattr command to make the scripts immutable.

# Burn It All
![Screenshot](https://img.shields.io/badge/Language-Bash-blue)
![Screenshot](https://img.shields.io/badge/Platform-Linux-brightgreen)

https://github.com/ciwen3/Public/blob/master/Bash/BurnItAll/BurnItAll.sh

I helped a company with an infection, we figured out it was known as XCSSET. In my research of the Malware we found and the information online I put together a script to systematically download each version of the Malware from each server they have check its SHA256 hash against a list of already downloaded malware and if it is unique (to me) upload it to virus total. 

# Job Search
![Screenshot](https://img.shields.io/badge/Language-Bash-blue)
![Screenshot](https://img.shields.io/badge/Platform-Linux-brightgreen)

https://github.com/ciwen3/Public/blob/master/Bash/job-search.sh

A fake script I wrote as a joke when looking for jobs. 


# Clone a Website for Offline Viewing

Great for capturing an unprotected webserver full of malicious stuff. 
```
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent http://example.org
```

    --mirror – Makes (among other things) the download recursive.
    --convert-links – Convert all the links (also to stuff like CSS stylesheets) to relative, so it will be suitable for offline viewing.
    --adjust-extension – Adds suitable extensions to filenames (html or css) depending on their content-type.
    --page-requisites – Download things like CSS style-sheets and images required to properly display the page offline.
    --no-parent – When recursing do not ascend to the parent directory. It useful for restricting the download to only a portion of the site.
    
    
    
### another suggestion: 
```
wget -mpHkKEb -t 1 -e robots=off -U 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0' http://www.example.com
```
    –m (--mirror) : turn on options suitable for mirroring (infinite recursive download and timestamps).
    -p (--page-requisites) : download all files that are necessary to properly display a given HTML page. This includes such things as inlined images, sounds, and referenced stylesheets.
    -H (--span-hosts): enable spanning across hosts when doing recursive retrieving.
    –k (--convert-links) : after the download, convert the links in document for local viewing.
    -K (--backup-converted) : when converting a file, back up the original version with a .orig suffix. Affects the behavior of -N.
    -E (--adjust-extension) : add the proper extension to the end of the file.
    -b (--background) : go to background immediately after startup. If no output file is specified via the -o, output is redirected to wget-log.
    -e (--execute) : execute command (robots=off).
    -t number (--tries=number) : set number of tries to number.
    -U (--user-agent) : identify as agent-string to the HTTP server. Some servers may ban you permanently for recursively download if you send the default User Agent.

