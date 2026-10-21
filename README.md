Python Network Scanner & Packet Analyzer

A beginner-friendly cybersecurity project built with Python, Socket, and Scapy to check TCP port connectivity and capture network packets for basic analysis.

Features

- TCP Port Checking: Uses Python's "socket" module to check whether a target host's TCP port accepts connections.
- Packet Capture: Uses Scapy's "sniff()" function to capture network packets.
- TCP Packet Filtering: Filters captured traffic to focus on TCP packets.
- Packet Summaries: Displays brief summaries of captured packets, including available IP addresses, ports, and TCP information.

Technologies Used

- Python
- Socket
- Scapy
- TCP/IP Networking

Installation

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/python-network-scanner-packet-analyzer.git

2. Navigate to the project directory

cd python-network-scanner-packet-analyzer

3. Install Scapy

pip install scapy

Usage

Run the Python script:

python main.py

The script attempts to connect to the configured host and port using a TCP socket. It then captures five TCP packets visible to Scapy and prints their summaries.

Example Output

Port is open
Capturing 5 TCP packets...
Ether / IP / TCP ...
Ether / IP / TCP ...

Actual output depends on the target's availability and the network traffic captured.

How It Works

1. Creates a TCP socket using Python's "socket" module.
2. Attempts a connection to the specified host and port.
3. Reports whether the connection succeeded.
4. Uses Scapy to capture five TCP packets.
5. Displays a summary of each captured packet.

Learning Outcomes

- Understanding Python socket programming.
- Learning TCP port connectivity checks.
- Capturing and inspecting network packets using Scapy.
- Applying Python functions, conditions, and imported libraries to network security.

Disclaimer

This project is intended for educational purposes and authorized security testing only. Scan only systems you own or have explicit permission to test. Capture network traffic only where you are authorized to do so.

Author

Cybersecurity Enthusiast | Python | Network Security
