import socket

def scan_ports(target):
    print(f"Scanning ports on {target}...")
    for port in range(1, 100):  # Scan first 100 ports
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"✅ Port {port} is open")
            s.close()
        except:
            pass
