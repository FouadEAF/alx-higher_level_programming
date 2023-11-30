#!/bin/bash
# Script that make a request to cause an specific response
curl -sL "http://0.0.0.0:5000/catch_me" -X PUT -H "Origin:You got me!"
