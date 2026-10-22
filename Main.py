import socket
from scapy.all import sniff, IP, TCP, UDP, ICMP, DNS

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

# Part 2: Scapy captures network packets
def packet_callback(packet):
    if IP in packet:
        if TCP in packet:
            print("TCP Packet:", packet.summary())

        elif UDP in packet and DNS in packet:
            print("DNS Packet:", packet.summary())

        elif UDP in packet:
            print("UDP Packet:", packet.summary())

        elif ICMP in packet:
            print("ICMP Packet:", packet.summary())


print("Capturing network packets...")
print("Protocols: TCP, UDP, ICMP, DNS")

sniff(
    filter="ip",
    count=20,
    prn=packet_callback
)
