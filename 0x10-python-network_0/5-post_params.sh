#!/bin/bash
#  script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -X POST -F 'email=test@gmail.com' -F 'Subject=I will always be here for PLD' "$1"
