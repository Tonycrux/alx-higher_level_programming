#!/bin/bash
# prints the content length of a header
# of a get requests using curl

curl -Is "$1" |grep "Content-Length:"| cut -d' ' -f2

