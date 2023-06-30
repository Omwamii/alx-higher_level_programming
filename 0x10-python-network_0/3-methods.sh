#!/usr/bin/bash
# script to display all HTTP methods accepted by server
curl -s -I -X OPTIONS "$1" | grep -i "^Allow:" | cut -d " " -f 2
