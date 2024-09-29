# Egy egyszer sített CHAT rendszert kezel hálózati szerver definíciója. ű ő
# thread-eket használ a klienskapcsolatok párhuzamos kezelésére.

HOST = '192.168.0.235'
PORT = 40000

import socket, sys, threading

class ThreadClient(threading.Thread):
    '''thread-objektum leszármaztatása a klienssel való kapcsolat kezeléséhez'''
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn

    def run(self):
        # Párbeszéd a klienssel :
        nom = self.getName() # Minden thread-nek neve van
        while 1:
            msgClient = self.connexion.recv(1024)
            if msgClient.upper() == "FIN" or msgClient =="":
                break
            message = "%s> %s" % (nom, msgClient)
            print (message)
            # Az üzenetet kiküldi az összes többi kliensnek :
            for cle in conn_client:
                if cle != nom: # ne küldje el a kibocsátónak
                    conn_client[cle].send(message)

        # A kapcsolat zárása :
        self.connexion.close() # a serveroldali kapcsolat megszakítása
        del conn_client[nom] # törli a bejegyzését a szótárban
        print ("Kliens %s lekapcsolódott." % nom)

# A thread itt fejez dik be ő
# A server inicializálása  Socket létrehozása :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print ("A socket összekapcsolása a választott címmel meghiúsult.")
    sys.exit()
print ("A server kész, várakozás a kérésekre ...")
mySocket.listen(5)
# A kliensek által kért kapcsolatok várása és kezelése :
conn_client = {} # a klienskapcsolatok szótára
while 1:
    connexion, adresse = mySocket.accept()
    # Új thread-objektum létrehozása a kapcsolat kezelésére :
    th = ThreadClient(connexion)
    th.start()
    # A kapcsolat tárolása a szótárban :
    it = th.getName() # thread-azonosító
    conn_client[it] = connexion
    print ("Kliens %s felkapcsolódott, IP cím %s, port %s." %\
    (it, adresse[0], adresse[1]))
    # Párbeszéd a klienssel :
    connexion.send("Ön felkapcsolódott. Küldje el az üzeneteit.")