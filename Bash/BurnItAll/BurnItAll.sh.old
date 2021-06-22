#!/bin/bash

# wrote this script to automate the process of downloading all the Malicious Files for XCSSET
# the files will then be uploaded to virustotal to burn all the hard work that the Malware writter is doing
# run as often as you'd like to annoy the Malware author
# each time his stuff is upload to virus total he will have to make changes so that his Malware is not easily flagged 


# Date variable
savetime=$(date +"%d-%b-%Y") 

for num in {1..300}; do

# create a text file to track file SHA256 hashes
if [[ $(ls | grep SHA256-Check.txt) == "" ]]; then touch SHA256-Check.txt; fi

if [[ $(ls $(date +"%d-%b-%Y") ) == "" ]]; then mkdir $(date +"%d-%b-%Y"); else mv $(date +"%d-%b-%Y") $(date +"%d-%b-%Y")-old; mkdir $(date +"%d-%b-%Y"); fi
cd $(date +"%d-%b-%Y")

echo "" >> ../SHA256-Check.txt 
echo $(date) >> ../SHA256-Check.txt 

# Servers to test Array 
server_array=( revokecert.ru icloudserv.ru nodeline.xyz linebrand.xyz mantrucks.xyz sidelink.xyz monotel.xyz atecasec.com atecasec.info icloudserv.com titiez.com adobestats.com flixprice.com statsmag.xyz statsmag.com adoberelations.com findmymacs.com trendmicronano.com findmymacs.com Titian.com pandminc.com)

# Empty arrays to track servers
down_array=()
up_array=()

# ping test servers
for p in ${server_array[@]}; do if [[ $(ping -c 1 $p | grep " 0% packet loss") == "" ]]; then down_array+="$p "; else up_array+="$p "; fi; done 

# start for loop on servers that are currently up
for s in ${up_array[@]}; do 

# create folder to track which server the downloads came from
mkdir $s
cd $s

# One off downloads
curl --max-time 5 -o a -k https://$s/a
curl -k -o project.xworkspace https://$s/agent/bin/frameworks.php?git&podsname=project.xworkspace\ --create-dir
curl -sk -d 'user=root&build_vendor=default&build_version=1' https://$s/apple/com.php -o a.osacompile

# first download array 
# (786) 545-7301-Saisd.net.html (786) 412-4567-Hanglung.com.html
test_array=(cat Pods agentd edged braved operad speedd firefoxd operad yandexd open)
# for loop of downloads from first array
for i in ${test_array[@]}; do curl -k -o $i https://$s/agent/bin/$i; sleep 10; done

# second download array
test2_array=(chrome_remote.applescript replicator.applescript safari_remote.applescript pods_infect.applescript screen_sim.applescript bootstrap.applescript opera_remote.applescript firefox_remote.applescript brave_remote.applescript  yandex_remote.applescript chromium_remote.applescript 360_remote.applescript )

# for loop of downloads from second array
for b in ${test2_array[@]}; do curl -k -o $b https://$s/agent/scripts/$b; sleep 10; done

# clean up downloads by removing useless things
for r in $(ls); do if [[ $(ls -lh $r | awk '{print $5}') == 162 ]]; then rm $r; fi; done  

# check if SHA256 hash has been seen before
# if so delete the file? or at least don't upload to virus total
# else append to SHA256-Check.txt
for h in $(ls); do if [[ $(cat ../../SHA256-Check.txt | grep $(sha256sum $h | awk '{print $1}')) == "" ]]; then sha256sum $h >> ../../SHA256-Check.txt; else rm $h; fi; done

# upload files to virus total
for u in $(ls); do curl --request POST  --url https://www.virustotal.com/api/v3/files --header 'x-apikey: d1d6c5a461bd1a72f81d3388d9e25442fc87adbb581ebe942df2bfd7da18f3a4' --form file=@$u -o VirusTotal-$u-upload.txt; done

# clean up Virus total txt
for i in $(ls VirusTotal-*.txt); do cat $i >> VirusTotal.txt; done 
rm -f VirusTotal-*.txt

# go back to the folder we started from
cd ..
# end for s in ${server_array[@]} loop
done 

# add a zip fold $s to conserve on space
cd ..
# tar --remove-files -caf $(date +"%d-%b-%Y").tgz $(date +"%d-%b-%Y")
tar --remove-files -caf $savetime-$num.tgz $savetime

done
