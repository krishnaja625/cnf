import socket
import threading

clientRunning = True
host = '10.10.8.228'  
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
rollnum = input("--> ")
roll_no = "MARK-ATTENDANCE " + rollnum 
s.send(roll_no.encode())

while clientRunning:
	mgs = s.recv(1024).decode()
    messge = mgs.split('')
    print(mgs)
    if messge[0] == 'SECRETQUESTION':
    	ans = input("--> ")
        s.send(("SECRETANSWER "+ans).encode())
    elif messge[0] == "ATTENDANCE-SUCCESS":
        print("closing")
    elif messge[0] == "ATTENDANCE-FAILURE":
        s.send(roll_no.encode())
    else:
        rollnum = input("--> ")
        roll_no = "MARK-ATTENDANCE " + rollnum 
        s.send(roll_no.encode())
s.close()