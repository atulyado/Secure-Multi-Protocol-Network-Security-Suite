import socket
import datetime

# Configuration
HOST = "localhost"
PORT = 42000

def log_to_file(client_ip, request, result):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("server_logs.txt", "a") as f:
        log_entry = f"[{timestamp}] IP: {client_ip} | REQ: {request} | RES: {result}\n"
        f.write(log_entry)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"[*] Secure Server listening on {PORT}...")

while True:
    conn, addr = server.accept()
    try:
        data = conn.recv(1024).decode().strip()
        if not data: continue

        # STEP 1 & 3: Structured Commands (e.g., "ADD 10 20")
        parts = data.split()
        command = parts[0].upper()
        x = int(parts[1])
        y = int(parts[2])

        # STEP 4: Logic & Error Handling
        if command == "ADD": result = x + y
        elif command == "SUB": result = x - y
        elif command == "MUL": result = x * y
        elif command == "DIV":
            result = x / y if y != 0 else "Error: Div by Zero"
        else:
            result = "Error: Unknown Command"

        # STEP 5: Logging
        log_to_file(addr[0], data, result)
        
        print(f"StudentID: 6788148 | Handled {command} for {addr}")
        conn.send(str(result).encode())

    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print(f"[!] {error_msg}")
        conn.send(error_msg.encode())
    
    finally:
        conn.close()