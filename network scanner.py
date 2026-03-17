import subprocess
from concurrent.futures import ThreadPoolExecutor

# Use your IP right here. Example 182.19.1. the last digit is no necessary here
network = "192.168.0."

def ping(ip):
    try:
        result = subprocess.run(
            ["ping", "-n", "1", "-w", "100", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if result.returncode == 0:
            print(f"[+] {ip} está activa")
    except:
        pass

print("Escaneando la red...\n")

with ThreadPoolExecutor(max_workers=50) as executor:
    for i in range(1, 255):
        ip = network + str(i)
        executor.submit(ping, ip)

print("\nEscaneo terminado.")
