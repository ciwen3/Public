#!/bin/bash

# wrote this script to automate the process of downloading all the Malicious Files for XCSSET
# the files will then be uploaded to virustotal to burn all the hard work that the Malware writter is doing
# run as often as you'd like to annoy the Malware author
# each time his stuff is upload to virus total he will have to make changes so that his Malware is not easily flagged 


# create a text file to track file SHA256 hashes
#if [[ $(ls | grep SHA256-Check.txt) == "" ]]; then touch SHA256-Check.txt; fi

mkdir $(date +"%d-%b-%Y")-Titiez
cd $(date +"%d-%b-%Y")-Titiez

#echo "" >>  ~/Desktop/SHA256-Check.txt
#echo $(date)-Titiez.com >>  ~/Desktop/SHA256-Check.txt

# Servers Array 
server_array=( titiez.com findmymacs.com )


# start for loop on servers
for s in ${server_array[@]}; do 

# create folder to track which server the downloads came from
mkdir $s
cd $s

# One off downloads
curl --max-time 5 -o a -k https://$s/a
curl -k -o project.xworkspace https://$s/agent/bin/frameworks.php?git&podsname=project.xworkspace\ --create-dir

# first download array
test_array=( cat Pods agentd edged braved operad xcassets speedd firefoxd operad yandexd )
# for loop of downloads from first array
for i in ${test_array[@]}; do curl -k -o $i https://$s/agent/bin/$i; sleep 10; done

# clean up downloads by removing useless things
for r in $(ls); do if [[ $(ls -lh $r | awk '{print $5}') == 162 ]]; then rm $r; fi; done  

# check if SHA256 hash has been seen before
# if so delete the file? or at least don't upload to virus total
# else append to SHA256-Check.txt
for h in $(ls); do if [[ $(cat ~/Desktop/SHA256-Check.txt | grep $(sha256sum $h | awk '{print $1}')) == "" ]]; then sha256sum $h >> ~/Desktop/SHA256-Check.txt; else rm $h; fi; done


# create text file to track virus total uploads
#touch VirusTotal-Uploads.txt
# upload files to virus total
for u in $(ls); do curl --request POST  --url https://www.virustotal.com/api/v3/files --header 'x-apikey: d1d6c5a461bd1a72f81d3388d9e25442fc87adbb581ebe942df2bfd7da18f3a4' --form file=@$u -o VirusTotal-$u-upload.txt; done


# clean up Virus total txt
for i in $(ls VirusTotal-*.txt); do cat $i >> VirusTotal.txt; done 
rm -f VirusTotal-*.txt

# end for s in ${server_array[@]} loop
done  


