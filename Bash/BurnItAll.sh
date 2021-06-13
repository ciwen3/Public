#!/bin/bash

# wrote this script to automate the process of downloading all the Malicious Files for XCSSET
# the files will then be uploaded to virustotal to burn all the hard work that the Malware writter is doing
# run as often as you'd like to annoy the Malware author
# each time his stuff is upload to virus total he will have to make changes so that his Malware is not easily flagged 

# create a text file to track file SHA256 hashes
if [[ $(ls | grep SHA256-Check.txt) == "" ]]; then touch SHA256-Check.txt; fi

mkdir $(date +"%d-%b-%Y")
cd $(date +"%d-%b-%Y")

# Servers Array 
server_array=( nodeline.xyz linebrand.xyz mantrucks.xyz sidelink.xyz monotel.xyz atecasec.com icloudserv.com titiez.com adobestats.com flixprice.com statsmag.xyz statsmag.com adoberelations.com findmymacs.com trendmicronano.com Titian.com 46.101.126.33 82.148.30.108 94.130.27.189 95.179.160.42 marriageclose.orangeanswer.com 180.136.102.34.bc.googleusercontent.com pandminc.com)

down_array=()
up_array=()

for p in ${server_array[@]}; do if [[ $(ping -c 1 $p | grep " 0% packet loss") == "" ]]; then down_array+="$p "; else up_array+="$p "; fi; done 

# start for loop on servers
for s in ${up_array[@]}; do 

# create folder to track which server the downloads came from
mkdir $s
cd $s

# One off downloads
curl --max-time 5 -o a -k https://$s/a
curl -k -o project.xworkspace https://$s/agent/bin/frameworks.php?git&podsname=project.xworkspace\ --create-dir

# first download array
test_array=(cat Pods agentd edged braved operad xcassets speedd firefoxd operad yandexd 7za)
# for loop of downloads from first array
for i in ${test_array[@]}; do curl -k -o $i https://$s/agent/bin/$i; sleep 10; done

# second download array
#test1_array=(7za Safari.zip Safari_Mojave.zip)
# for loop of downloads from second array
#for a in ${test1_array[@]}; do curl -k -o $a https://$s/agent/bin/$a; sleep 10; done

# third download array
test2_array=(chrome_remote.applescript replicator.applescript safari_remote.applescript pods_infect.applescript screen_sim.applescript bootstrap.applescript opera_remote.applescript firefox_remote.applescript brave_remote.applescript  yandex_remote.applescript chromium_remote.applescript 360_remote.applescript)
# for loop of downloads from third array
for b in ${test2_array[@]}; do curl -k -o $b https://$s/agent/scripts/$b; sleep 10; done

# clean up downloads by removing useless things
for r in $(ls); do if [[ $(ls -lh $r | awk '{print $5}') == 162 ]]; then rm $r; fi; done  


# check if SHA256 hash has been seen before
# if so delete the file? or at least don't upload to virus total
# else append to SHA256-Check.txt
for h in $(ls); do if [[ $(cat ../../SHA256-Check.txt | grep $(sha256sum $h | awk '{print $1}')) == "" ]]; then sha256sum $h >> ../../SHA256-Check.txt; else rm $h; fi; done


# create text file to track virus total uploads
#touch VirusTotal-Uploads.txt
# upload files to virus total
for u in $(ls); do curl --request POST  --url https://www.virustotal.com/api/v3/files --header 'x-apikey: <API_KEY>' --form file=@$u -o VirusTotal-$u-upload.txt; done


# clean up Virus total txt
for i in $(ls VirusTotal-*.txt); do cat $i >> VirusTotal.txt; done 

# go back to the folder we started from
cd ..
# add a zip fold $s to conserve on space
# see if there are other places we can uplaod the files for investigation
# end for s in ${server_array[@]} loop
done  

