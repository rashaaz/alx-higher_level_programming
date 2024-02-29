#!/bin/bash
#end a POST request to the URL with specified parameters
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
