# Egy elemi hálózati kliens definíciója

# A kliens egy ad hoc serverrel folytat párbeszédet
import socket, sys
HOST = '192.168.14.152'
PORT = 50000

# 1) socket létrehozása :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2) kapcsolatkérés küldése a serverhez :
try:
    mySocket.connect((HOST, PORT))
except socket.error:
    print ("A kapcsolat meghiúsult.")
    sys.exit()
print ("A kapcsolat létrejött a serverrel.")

# 3) Párbeszéd a serverrel :
msgServeur = mySocket.recv(1024)
while 1:
    if msgServeur.upper() == "FIN" or msgServeur =="":
        break
    print ("S>", msgServeur)
    msgClient = input("C> ")
    mySocket.send(msgClient)
    msgServeur = mySocket.recv(1024)
# 4) A kapcsolat zárása :
print ("A kapcsolat megszakítva.")
mySocket.close()