import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    # Try to connect to a specific port on a given IP address
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
        
            # Try to connect to the target IP and port
            result = s.connect_ex((ip, port))
        
            # '0' means port is open
            if result == 0:
                print(f" [+] Port {port} is open!")
    
    except Exception as e:
        print(f"Error scanning port {port} : {e}")
    

def main():
    print("SIMPLE PORT SCANNER: ")
    
    ip = input("Enter the target IP Address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    print(f"\n Scanning {ip} from port {start_port} to {end_port} ...\n")
    
    # Use ThreadPoolExecutor to speed up scanning
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port)
            
    print("\n Scanning completed!")
    
if __name__ == "__main__":
    main()