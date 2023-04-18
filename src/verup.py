import requests
import os
import re
import subprocess
import time
from bs4 import BeautifulSoup

version_now = "1.2"
repo = "https://github.com/hcosm1c/ddos/blob/main/version.txt"
req = requests.get(repo)

https = BeautifulSoup(req.content, 'html.parser')
upt = https.find(class_='blob-code blob-code-inner js-file-line').get_text()

def gitve():
    if upt == version_now:
        os.system("clear")
    else:
        print("SOURCE DESATUALIZADO, ATUALIZANDO...")
        os.chdir("/root")
        os.system("rm -rf ddos")
        time.sleep(1)
        os.system("git clone https://github.com/hcosm1c/ddos")
        os.system("clear")