import socket
import signal

def signal_handler(sig, frame):
        print("socket closed\n")
        sockd.close()
        exit()

sockd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = "192.168.56.101"
port = 8888

print("Welcome to hostName to IPaddress v0.1.")
print("Enter URL(e.g google.com) to start or 0 to quit.")
signal.signal(signal.SIGINT,signal_handler)
while True:
        url = input("URL: ")
        if url == "0":
                sockd.close()
                exit()
        msg = bytes(url,'utf-8')
        sent = sockd.sendto(msg,(host,port))
        data,addr = sockd.recvfrom(1024)
        print("IP Address: {0}".format(data.decode('utf-8')))

