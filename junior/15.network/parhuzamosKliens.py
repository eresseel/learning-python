# Üzenetek párhuzamos kibocsátását és fogadását kezel ő
# hálózati kliens definiálása (2 THREAD alkalmazása).

host = '192.168.0.235'
port = 40000

import socket, sys, threading

class ThreadReception(threading.Thread):
    """üzenetek fogadását kezel thread objektum"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn # a kapcsolati socket referenciája   

    def run(self):
        while 1:
            message_recu = self.connexion.recv(1024)
            print ("*" + message_recu + "*")
            if message_recu =='' or message_recu.upper() == "FIN":
                break
            # A <fogadás> thread itt fejez dik be. ő
            # Kényszerítjük a <kibocsátás> thread lezárását :
            th_E._Thread__stop()
            print ("Leállt a kliens. Kapcsolat megszakítva.")
            self.connexion.close()  

class ThreadEmission(threading.Thread):
    """üzenetek kibocsátását kezel thread objektum"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn # a kapcsolati socket referenciája  

    def run(self):
        while 1:
            message_emis = raw_input()
            self.connexion.send(message_emis)  

# F program  Kapcsolat létrehozása : ő
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connexion.connect((host, port))
except socket.error:
    print ("A kapcsolat meghiúsult.")
    sys.exit()
    print ("A kapcsolat létrejött a serverrel.")

# Párbeszéd a server-rel : két thread-et indítunk az üzenetek
# fogadásának és indításának egymástól független kezelésére :
th_E = ThreadEmission(connexion)
th_R = ThreadReception(connexion)
th_E.start()
th_R.start() 