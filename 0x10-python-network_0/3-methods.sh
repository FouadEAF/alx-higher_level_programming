#!/bin/bash
# Script that take an URL and show the Allowed option
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
