**Python Network Scanner & Packet Analyzer**

A beginner-friendly Python cybersecurity project that checks TCP port connectivity and captures network packets using Python's "socket" module and Scapy.

**Features**

- TCP Port Checking: Checks connectivity to a target host on a specified TCP port.
- Packet Capture: Captures up to 20 packets visible on the selected network interface.
- Protocol Identification: Identifies TCP, UDP, ICMP, and DNS traffic over IPv4.
- IP Address Analysis: Displays source and destination IP addresses.
- Packet Summaries: Uses Scapy to display packet details for basic network analysis.

**Technologies Used**

- Python
- Socket
- Scapy
- Npcap (Windows packet capture)

**Requirements**

- Python 3
- Scapy
- Npcap on Windows for packet capture

**Installation**

Install Scapy:

pip install scapy

On Windows, install Npcap from the official website:

https://npcap.com/#download

**Usage**

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Save the Python code in "networkscanner.py".
4. Run the script: python networkscanner.py
5. Allow the required permissions for packet capture if prompted.

**How It Works**

1. The "socket" module attempts a TCP connection to the specified host and port.
2. Scapy captures up to 20 IPv4 packets using "filter="ip"".
3. The callback function checks for IP, TCP, UDP, DNS, and ICMP layers.
4. Source IP addresses, destination IP addresses, and packet summaries are printed to the terminal.

**Learning Outcomes**

- Understanding TCP socket connections and port checks
- Learning basic packet capture with Scapy
- Identifying common network protocols
- Inspecting source and destination IP addresses
- Practicing Python for network analysis

Disclaimer

Use this project only on systems and networks you own or have explicit permission to test. Packet capture may require administrator privileges and Npcap on Windows.
