import requests
import os
import re
from bs4 import BeautifulSoup

#GITVE
repo = "https://github.com/hcosm1c/ddos/blob/main/version.txt"
req = requests.get(repo)

https = BeautifulSoup(req.content, 'html.parser')
upt = https.find(class_='blob-code blob-code-inner js-file-line').get_text()

def gitve():
    if upt == "1.1":
        print("SOURCE ATUALIZADO")
    else:
        print("SOURCE DESATUALIZADO")

gitve()

#INICIAR
exec(requests.get("https://raw.githubusercontent.com/hcosm1c/ddos/main/src/menu.py").text)
