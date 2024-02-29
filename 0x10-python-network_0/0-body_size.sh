#!/bin/bash
# Send a GET request to the URL and retrieve the body size in bytes
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
