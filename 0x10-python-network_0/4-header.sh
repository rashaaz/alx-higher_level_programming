#!/bin/bash
# Send a GET request to the URL with the custom header
curl -sH "X-School-User-Id: 98" "$1"
