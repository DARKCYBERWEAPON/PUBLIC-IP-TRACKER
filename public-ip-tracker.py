#TOOL CREATED BY DARK_CYBER_WEAPON. /// ALL RIGHTS RESERVED BY DARK CYBER WEAPON.  (((ASANKA; L; ROOPASINGHE;./)))
import requests
import pprint
import sys ,shutil ,time
from time import sleep
import os
os.system("clear")
R = '\033[91m \033[01m'
G = '\033[92m \033[01m'
B = '\033[94m \033[01m'
C = '\033[36m \033[01m'
N = '\033[0m \033[01m'
logo = """
╭━━━┳╮╱╭┳━━╮╭╮╱╱╭━━┳━━━╮╭━━┳━━━╮╭━━━━┳━━━┳━━━┳━━━┳╮╭━┳━━━┳━━━╮
┃╭━╮┃┃╱┃┃╭╮┃┃┃╱╱╰┫┣┫╭━╮┃╰┫┣┫╭━╮┃┃╭╮╭╮┃╭━╮┃╭━╮┃╭━╮┃┃┃╭┫╭━━┫╭━╮┃
┃╰━╯┃┃╱┃┃╰╯╰┫┃╱╱╱┃┃┃┃╱╰╯╱┃┃┃╰━╯┃╰╯┃┃╰┫╰━╯┃┃╱┃┃┃╱╰┫╰╯╯┃╰━━┫╰━╯┃
┃╭━━┫┃╱┃┃╭━╮┃┃╱╭╮┃┃┃┃╱╭╮╱┃┃┃╭━━╯╱╱┃┃╱┃╭╮╭┫╰━╯┃┃╱╭┫╭╮┃┃╭━━┫╭╮╭╯
┃┃╱╱┃╰━╯┃╰━╯┃╰━╯┣┫┣┫╰━╯┃╭┫┣┫┃╱╱╱╱╱┃┃╱┃┃┃╰┫╭━╮┃╰━╯┃┃┃╰┫╰━━┫┃┃╰╮
╰╯╱╱╰━━━┻━━━┻━━━┻━━┻━━━╯╰━━┻╯╱╱╱╱╱╰╯╱╰╯╰━┻╯╱╰┻━━━┻╯╰━┻━━━┻╯╰━╯"""
print(C)
print(logo)
print(N)
print("")
print(R)
print("[+] TOOL CREATED BY DARK CYBER WEAPON [+]")
m = """
▀█▀ █▀█ █▀█ █░░   █▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀▀ █▀▄   █▄▄ █▄█   █▀▄ ▄▀█ █▀█ █▄▀   █▀▀ █▄█ █▄▄ █▀▀ █▀█   █░█░█ █▀▀ ▄▀█ █▀█ █▀█ █▄░█
░█░ █▄█ █▄█ █▄▄   █▄▄ █▀▄ ██▄ █▀█ ░█░ ██▄ █▄▀   █▄█ ░█░   █▄▀ █▀█ █▀▄ █░█   █▄▄ ░█░ █▄█ ██▄ █▀▄   ▀▄▀▄▀ ██▄ █▀█ █▀▀ █▄█ █░▀█"""
for x in m:
       for y in x:
             print(y,end='')
             sys.stdout.flush()
             time.sleep(0.01)
print ()
print("")
print("")
print(G)
ip = str(input("ENTER TARGET PUBLIC IP ADDRESS HERE:::> "))
print("")
print("")
print(B)
url = f"https://ipapi.co/{ip}/json/"
r = requests.get(url)
pprint.pprint(r.json())
print("")
