import socket
from scapy.all import sniff, IP, TCP

# Part 1: Socket checks a port
host = "scanme.nmap.org"
port = 80

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
sock.settimeout(3)

result = sock.connect_ex((host, port))

if result == 0:
    print("Port is open")
else:
    print("Connection failed")

sock.close()


# Part 2: Scapy captures TCP packets
def packet_callback(packet):
    if IP in packet and TCP in packet:
        print(packet.summary())


print("Capturing 5 TCP packets...")
sniff(
    filter="tcp",
    count=5,
    prn=packet_callback
)
