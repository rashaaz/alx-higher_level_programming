# 0x11. Python - Network #1

## Description
This repository contains Python scripts created as part of the "Python - Network #1" project at Holberton School. The scripts demonstrate various network programming concepts in Python, including fetching internet resources, handling HTTP requests, and interacting with APIs.

## Learning Objectives
At the end of this project, students are expected to be able to explain the following concepts without the help of Google:
- How to fetch internet resources with the Python package urllib
- How to decode urllib body response
- How to use the Python package requests
- How to make HTTP GET requests
- How to make HTTP POST/PUT/etc. requests
- How to fetch JSON resources
- How to manipulate data from an external service

## Project Tasks Overview
- **0. What's my status? #0**: Write a Python script that fetches https://alx-intranet.hbtn.io/status using urllib.
- **1. Response header value #0**: Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the X-Request-Id variable found in the header of the response.
- **2. POST an email #0**: Write a Python script that takes in a URL and an email, sends a POST request to the URL with the email as a parameter, and displays the body of the response.
- **3. Error code #0**: Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response. Handle urllib.error.HTTPError exceptions.
- **4. What's my status? #1**: Write a Python script that fetches https://alx-intranet.hbtn.io/status using the requests package.
- **5. Response header value #1**: Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the variable X-Request-Id in the response header.
- **6. POST an email #1**: Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response.
- **7. Error code #1**: Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response. Print an error message if the HTTP status code is greater than or equal to 400.
- **8. Search API**: Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
- **9. My GitHub!**: Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id.

## Requirements
- Allowed editors: vi, vim, emacs
- All scripts will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file at the root of the repository is mandatory
- Your code should use the pycodestyle (version 2.8.*) style
- All files must be executable
- The length of your files will be tested using wc
- All modules should have documentation
- You must use `get` to access dictionary value by key
- A documentation is not a simple word, it’s a real sentence explaining the purpose of the module, class, or method
- Your code should not be executed when imported
- The scripts must meet specific requirements mentioned in each task

## Resources
Read or watch:
- [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
- [Quickstart with Requests package](https://docs.python-requests.org/en/latest/user/quickstart/)
- [Requests package](https://docs.python-requests.org/en/latest/)

## Project Timeline
- Project starts: Mar 1, 2024 6:00 AM
- Project ends: Mar 2, 2024 6:00 AM
- Checker release: Mar 1, 2024 12:00 PM
- An auto-review will be launched at the deadline

## Copyright - Plagiarism
All solutions for the tasks must be created independently. Plagiarism in any form is strictly forbidden and will result in removal from the program.


