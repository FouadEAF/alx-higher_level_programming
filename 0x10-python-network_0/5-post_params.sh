#!/bin/bash
# Script that send a POST request and display the body response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
