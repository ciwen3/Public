#!/bin/bash

for newjob in $(cat jobsearch); do 
	if [[ work-life-balance -gt mental-health-needs ]] 
    then
	    if [[ pay-benefits -gt cost-of-living ]] 
        then
	        if [[ job-education -eq my-interests ]] 
            then
	            if [[ job-advancement -eq deserverd ]] 
                then
	                if [[ $newjob -eq expectations ]]
                    then
                        echo "I accept $newjob" > response-email
                        sendmail newboss@greatjob.com < response-email
                    fi
                fi
            fi
        fi
    fi
done
