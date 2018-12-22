import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.10.8.228'
port = 5000
Server = True
clients = {}
s.bind((host, port))
s.listen()
ans = ""
file = open('data.csv')
datafile = file.read()
file.close()
dictionary_data = {}
line = datafile.split("\n")
for i in line:
	words = i.split(",")
	dictionary_data[0] = [words[1], words[2]]
def secrtques():
    connected = True
    rollno  = 0
    while connected:
        mgss = client.recv(1024).decode()
        messages = mgss.split(" ")
        if messages[0] == "MARK-ATTENDANCE":
            if dictionary_data.get(messages[1]) is not None:
                client.send(("SECRETQUESTION "+dictionary_data[messages[1]][0]).encode())
                rollno = messages[1]
            else:
                client.send("ROLLNUMBER-NOTFOUND")
        elif messages[0] == "SECRETANSWER":
            if messages[1] == dictionary_data[rollno][1]:
                client.send("ATTENDANCE-SUCCESS")
            else:
                client.send("ATTENDANCE-FAILURE")
    client.close()

print("Server is running.")
while Server:
    client, adrs = s.accept()
    threading.Thread(target = secrtques, args = (uname, client, )).start()