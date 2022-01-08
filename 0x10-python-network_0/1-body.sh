#!/bin/bash
# pritns the body of a request if the status code 
# is 200 using curl

response=$(curl -s -w "\nSTATUS_CODE:%{http_code}" "$1")
status_=$(echo "$response"| grep "STATUS_CODE"|cut -d":" -f2)

if [[ "$status_" -eq "200" ]]
then
  echo "$response"|grep -v "STATUS_CODE"
fi
