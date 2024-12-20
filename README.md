# Network Ping Utility

This Python-based tool allows you to ping a specific IP address and port using both **TCP** and **UDP** protocols, displaying real-time round-trip times for each protocol. It can also automatically detect whether the connection is available using either TCP or UDP and show the results in a color-coded output for easy visualization.

### Features:
- Supports **TCP** and **UDP** protocols.
- **Multi-threaded** to run TCP and UDP pings simultaneously.
- **Real-time** display of round-trip times for each protocol.
- **Color-coded output** to differentiate between successful connections, errors, and time statistics.
- **Automatic protocol detection** (TCP/UDP) based on connectivity.

---

Enter the IP address: 192.168.1.1
Enter the port: 80

Checking connection for 192.168.1.1:80 via TCP...
Connection established successfully with 192.168.1.1:80 via TCP.

Starting to ping 192.168.1.1:80 using TCP...

Connected to 192.168.1.1:80 via TCP protocol. time=15.35ms
Connected to 192.168.1.1:80 via TCP protocol. time=14.92ms
...
