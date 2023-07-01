#!/bin/bash
# script to send request and display status code
curl -s -L -o /dev/null -w "%{http_code}" "$1"
