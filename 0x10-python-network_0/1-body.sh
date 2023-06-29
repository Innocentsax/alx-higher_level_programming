i#!/bin/bash
# Takes a URL, sends a GET request to the URL, and displays body of the response
curl -Lsf "$1"
