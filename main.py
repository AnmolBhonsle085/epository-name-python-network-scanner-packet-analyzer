import socket
from scapy.all import sniff, IP, TCP


# Part 1: Check TCP port connectivity using a socket
def check_tcp_port(host, port):
    print(f"Checking {host}:{port} ...")

    # Create a TCP socket using IPv4
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wait no longer than 3 seconds for a blocking socket operation
    sock.settimeout(3)

    try:
        result = sock.connect_ex((host, port))

        if result == 0:
            print(f"TCP port {port} accepts connections on {host}.")
        else:
            print(f"Connection to {host}:{port} failed (error code: {result}).")
            print("A failed connection does not always mean the port is closed.")

    except socket.gaierror:
        print(f"Could not resolve hostname: {host}")
    except socket.timeout:
        print(f"Connection to {host}:{port} timed out.")
    except OSError as error:
        print(f"Socket error: {error}")
    finally:
        sock.close()


# Part 2: Display summaries of captured IP/TCP packets
def packet_callback(packet):
    if IP in packet and TCP in packet:
        print(packet.summary())


def capture_tcp_packets(count=5):
    print(f"\nCapturing up to {count} TCP packets...")
    print("Press Ctrl+C to stop early.")

    try:
        sniff(filter="tcp", count=count, prn=packet_callback)
    except PermissionError:
        print("Permission denied. Packet capture may require administrator/root privileges.")
    except OSError as error:
        print(f"Packet capture error: {error}")


if __name__ == "__main__":
    # Use only systems you own or are authorized to test.
    target_host = "scanme.nmap.org"
    target_port = 80

    check_tcp_port(target_host, target_port)
    capture_tcp_packets(count=5)
