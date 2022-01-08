#!/bin/bash
# prints status code of a response
# to a curl request

curl -s -o /dev/null -w "%{http_code}\n" "$1"
