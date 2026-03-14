import socket
from concurrent.futures import ThreadPoolExecutor

target = input("IP objetivo: ")

# puertos comunes
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP"
}

print(f"\nEscaneando {target}...\n")

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:

            service = common_ports.get(port, "Desconocido")

            print(f"[+] Puerto {port} abierto ({service})")

            # banner grabbing
            try:
                s.send(b"HEAD / HTTP/1.0\r\n\r\n")
                banner = s.recv(1024).decode().strip()
                if banner:
                    print(f"    Banner: {banner[:100]}")
            except:
                pass

        s.close()

    except:
        pass


with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(1, 1025))

print("\nEscaneo terminado.")
