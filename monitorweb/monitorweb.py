# Monitor de conexão WEB

#import requests
import socket, ping

class MonitorWeb:

        localIP = ''

        def __init__(self):
                self.localIP = socket.gethostbyname(socket.gethostname())

        def __str__(self):
                return "MonitorWeb IP " + self.localIP

        def Ping(self, ip):
                ping.

mw = MonitorWeb()
print