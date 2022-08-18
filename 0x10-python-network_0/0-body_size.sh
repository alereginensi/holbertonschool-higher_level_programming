#!/bin/bash
# script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s https://code.jquery.com/jquery-3.1.1.min.js | wc -c
