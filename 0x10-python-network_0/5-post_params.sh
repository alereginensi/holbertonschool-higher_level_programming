#!/bin/bash
#  script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -sX POST "$1" -F "email=test@gmail.com" -F "Subject=I will always be here for PLD"
