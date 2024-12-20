import socket
import time
import threading
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Function to ping TCP protocol
def ping_tcp(ip, port):
    try:
        start_time = time.time()
        with socket.create_connection((ip, port), timeout=1):
            ping_time = (time.time() - start_time) * 1000  # Convert to milliseconds
            print(f"{Fore.WHITE}Connected to {ip}:{port} via {Fore.GREEN}TCP {Fore.WHITE}protocol. {Fore.GREEN}time={ping_time:.2f}ms")
    except (socket.timeout, socket.error) as e:
        print(f"{Fore.RED}Unable to connect to {ip}:{port} via TCP. Error: {e}")

# Function to ping UDP protocol
def ping_udp(ip, port):
    try:
        start_time = time.time()
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(1)  # Timeout after 1 second
            s.sendto(b'', (ip, port))  # Send an empty message
            s.recvfrom(1024)  # Wait for a response
            ping_time = (time.time() - start_time) * 1000  # Convert to milliseconds
            print(f"{Fore.WHITE}Connected to {ip}:{port} via {Fore.GREEN}UDP {Fore.WHITE}protocol. {Fore.GREEN}time={ping_time:.2f}ms")
    except (socket.timeout, socket.error) as e:
        print(f"{Fore.RED}Unable to connect to {ip}:{port} via UDP. Error: {e}")

# Function to check if the connection is available (TCP or UDP)
def check_connection(ip, port):
    try:
        # First try TCP
        print(f"{Fore.YELLOW}Checking connection for {ip}:{port} via TCP...")
        with socket.create_connection((ip, port), timeout=1):
            print(f"{Fore.GREEN}Connection established successfully with {ip}:{port} via TCP.")
            return 'TCP'
    except (socket.timeout, socket.error) as e:
        # If TCP fails, try UDP
        print(f"{Fore.RED}Connection failed for {ip}:{port} via TCP. Trying UDP... Error: {e}")
        try:
            # UDP doesn't establish a connection, so just sending a packet
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.settimeout(1)
                s.sendto(b'', (ip, port))
                s.recvfrom(1024)  # Wait for a response
            print(f"{Fore.GREEN}Connection established successfully with {ip}:{port} via UDP.")
            return 'UDP'
        except (socket.timeout, socket.error) as e:
            print(f"{Fore.RED}Connection failed for {ip}:{port} via UDP. Error: {e}")
            return None

# Function to continuously ping the IP with the detected protocol (with threading)
def ping(ip, port, protocol):
    while True:
        if protocol == 'TCP':
            threading.Thread(target=ping_tcp, args=(ip, port)).start()
        elif protocol == 'UDP':
            threading.Thread(target=ping_udp, args=(ip, port)).start()
        time.sleep(0.1)  # Adjust ping speed (in seconds)

# Main function
def main():
    ip = input("Enter the IP address: ")
    port = int(input("Enter the port: "))
    
    # Check the connection first
    protocol = check_connection(ip, port)
    
    if protocol:
        # If the connection was established, start pinging
        print(f"\n{Fore.YELLOW}Starting to ping {ip}:{port} using {protocol}...\n")
        ping(ip, port, protocol)
    else:
        print(f"{Fore.RED}Could not establish a connection to {ip}:{port} using either TCP or UDP.")

if __name__ == "__main__":
    main()
