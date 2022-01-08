#!/bin/bash
# sends a post request as a json
# file using curl

curl -sX POST -H "Content-type:application/json" -d @"$2" "$1"
