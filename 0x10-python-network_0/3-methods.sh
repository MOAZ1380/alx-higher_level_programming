#!/bin/bash
# Write a Bash script that takes in a URL and displays all HTTP methods the server
curl -sI -X OPTIONS "$1"
