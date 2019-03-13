#!/usr/bin/env bash

# Host tool is required on system for this to work.
# Script will check for A, PTR, MX
# Output is stored in results.txt

DOMAINS=$1
SUBDOMAINS=$2

#Argument checks
if [ $# -eq 0 ]
  then
    printf "$0 <domain_file> <subdomain_file>\n"
else
    touch results.txt

    # Forward DNS lookup
    printf "Starting forward DNS lookup..\n"
    for domain in $(cat $1)
    do
        printf "Looking up $domain\n"
        for subdomain in $(cat $SUBDOMAINS)
            do
                host $subdomain.$domain >> results.txt
        done
    done

    # Reverse DNS lookup
    printf "Starting reverse DNS lookup..\n"
    cat results.txt | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' | sort | uniq > ip_list.txt
    for ip in $(cat ip_list.txt)
    do
        host $ip | grep -v "not found" >> results.txt
    done

    printf "All done!\n"
    printf "Results:\n\n"
    cat results.txt
fi
