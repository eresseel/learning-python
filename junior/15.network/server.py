# Egy elemi hálózati server definíciója
# Ez a server várja a kapcsolatot a klienssel, hogy párbeszédet kezdjen vele
import socket, sys

HOST = '192.168.14.152'
PORT = 50000

# 1) A socket létrehozása:
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2) a socket összekapcsolása egy meghatározott címmel :
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print ("A socket összekapcsolása a választott címmel meghiúsult.")
    sys.exit()

while 1:
    # 3) Várakozás a kliens kapcsolatkérésére :
    print ("A server kész, a kérésre vár ...")
    mySocket.listen(5)

    # 4) A kapcsolat létrehozása :
    connexion, adresse = mySocket.accept()
    print ("A kliens felkapcsolódott, IP cím %s, port %s" % (adresse[0], adresse[1]))

    # 5) Párbeszéd a klienssel :
    connexion.send("Ön a Marcel serverre kapcsolódott. Küldje el az üzenetét.")
    msgClient = connexion.recv(1024)
    while 1:
        print ("C>", msgClient)
        if msgClient.upper() == "FIN" or msgClient =="":
            break
        msgServeur = input("S> ")
        connexion.send(msgServeur)
        msgClient = connexion.recv(1024)

    # 6) A kapcsolat zárása :
    connexion.send("Viszontlátásra !")
    print ("A kapcsolat megszakadt.")
    connexion.close()

    ch = input("<U>jrakezdeni <B>efejezni ? ")
    if ch.upper() =='B':
        break