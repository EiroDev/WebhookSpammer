import requests
import time
import os
from colored import fg, bg, attr
from os import system

os.system("clear")

color = fg('46') + bg('16')
res = attr('reset')
print(color + """.d8888b.  8888888888 888b    888  .d88888b.                                     
d88P  Y88b 888        8888b   888 d88P" "Y88b                                    
Y88b.      888        88888b  888 888     888                                    
 "Y888b.   8888888    888Y88b 888 888     888                                    
    "Y88b. 888        888 Y88b888 888     888                                    
      "888 888        888  Y88888 888     888                                    
Y88b  d88P 888        888   Y8888 Y88b. .d88P                                    
 "Y8888P"  8888888888 888    Y888  "Y88888P"                                     
                                                                                 
                                                                                 
                                                                                 
 .d8888b.  8888888b.     d8888 888b     d888 888b     d888 8888888888 8888888b.  
d88P  Y88b 888   Y88b   d88888 8888b   d8888 8888b   d8888 888        888   Y88b 
Y88b.      888    888  d88P888 88888b.d88888 88888b.d88888 888        888    888 
 "Y888b.   888   d88P d88P 888 888Y88888P888 888Y88888P888 8888888    888   d88P 
    "Y88b. 8888888P" d88P  888 888 Y888P 888 888 Y888P 888 888        8888888P"  
      "888 888      d88P   888 888  Y8P  888 888  Y8P  888 888        888 T88b   
Y88b  d88P 888     d8888888888 888   "   888 888   "   888 888        888  T88b  
 "Y8888P"  888    d88P     888 888       888 888       888 8888888888 888   T88b""" + res)

print ('%s%s \nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤBy Eiro | Seno. %s' % (fg('red'), bg('black'), attr('reset')))

print ('%s%s \nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ Discord ==> %s' % (fg('red'), bg('black'), attr('reset')))

print ('%s%s \nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ Github ==> %s' % (fg('red'), bg('black'), attr('reset')))

print ('%s%s \nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ Support me ==> %s' % (fg('red'), bg('black'), attr('reset')))

time.sleep(2)

x = 1

WEBHOOK_URL = str(input("\n\nEnter the webhook url : "))
WEBHOOK_USERNAME = str(input("\nChoose the webhook nickname : "))
WEBHOOK_AVATAR = str(input("\nChoose the webhook avatar : "))
WEBHOOK_CONTENT = str(input("\nWrite what you want to send : "))
SPAM = int(input("\nEnter the number of spam (Limited to 30 due to API) : "))

while x < SPAM:
    try:
        payload = {"content":WEBHOOK_CONTENT,"username":WEBHOOK_USERNAME,"avatar_url":WEBHOOK_AVATAR}
        r = requests.post(WEBHOOK_URL,data=payload)
        x +=1
        print("[+] Request sent")
    except:
        print("[-] Request not sent")
        pass
print("\n[+] Spam Done ✓")
