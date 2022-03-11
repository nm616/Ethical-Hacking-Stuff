#!/usr/bin/env python

import requests

target_url = ""
data_dict = {"username" : "blahblah", "password":"blahblah", "Login": "submit"}
response = requests.post(target_url, data=data_dict)
print(response.content)

