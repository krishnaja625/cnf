from threading import *
import socket
def main():
	s=socket.socket()

	host='10.10.8.228'
	port=6500
	s.connect((host,port))
	print(s.recv(1024).decode())
	s.send(input().encode())
	Thread(target= send,args=(s,)).start()
	while True:
		print(s.recv(1024).decode())
	s.close()
def send(s):
	while True:
		s.send(input().encode())
	s.close()
if __name__=='__main__':
	main()
