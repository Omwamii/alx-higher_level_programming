#!/usr/bin/bash
# script to send request to url and display size of body response
curl -so /dev/null "$1" -w '%{size_download}' ; echo ""
