import socket
from threading import *
def main():
	s = socket.socket()
	host='10.10.8.228'
	port=6500
	s.bind((host,port))
	s.listen(10)
	lis={}
	while True:
		c,addr=s.accept()
		c.send('Enter your name'.encode())

		usern=c.recv(1024).decode()
		print(usern+'is Connected.')
		lis[c]=usern
		Thread(target = chat,args=(lis,c)).start()
	s.close()
def chat(lis,c):
	while True:
		message=c.recv(1024).decode()
		if(message!='q'):
			for user,val in lis.items():
				if c != user:
					user.send((lis[c]+'-->'+message).encode())
				else:
					c.send(('yourmgs==>'+message).encode())
		else:
			c.close()
			lis.pop(c)
			return 1
if __name__=='__main__':
	main()


