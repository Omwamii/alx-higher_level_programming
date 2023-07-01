#!/bin/bash
# script to make request to server to get 'You got me!'
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
