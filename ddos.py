import requests
import os
import re
import subprocess
import time
from bs4 import BeautifulSoup



repo = "https://github.com/hcosm1c/ddos/blob/main/version.txt"
req = requests.get(repo)

https = BeautifulSoup(req.content, 'html.parser')
upt = https.find(class_='blob-code blob-code-inner js-file-line').get_text()

def gitve():
    if upt == "1.1":
        print("SOURCE ATUALIZADO")
    else:
        print("SOURCE DESATUALIZADO, ATUALIZANDO...")
        os.chdir("/root")
        os.system("rm -rf ddos")
        time.sleep(1)
        os.system("git clone https://github.com/hcosm1c/ddos")

gitve()

#INICIAR
exec(requests.get("https://raw.githubusercontent.com/hcosm1c/ddos/main/src/menu.py").text)
