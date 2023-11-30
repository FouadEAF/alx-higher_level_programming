#!/bin/bash
# Script that send a request and display only the status code
curl -o /dev/null -w "%{http_code}" -s "$1"
