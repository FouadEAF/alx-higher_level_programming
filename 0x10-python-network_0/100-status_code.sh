#!/bin/bash
# Script that send a request to a URL passed as an argument,
# and display only the status code of the response
curl -o /dev/null -w "%{http_code}" -s "$1"
