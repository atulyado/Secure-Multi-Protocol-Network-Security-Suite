import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 42000))

print("Commands: ADD, SUB, MUL, DIV (Example: MUL 5 10)")
cmd = input("Enter Command and two numbers: ")

client.send(cmd.encode())
result = client.recv(1024).decode()

print("-" * 30)
print(f"StudentID: 6788148")
print(f"Time: {time.asctime()}")
print(f"Server Response: {result}")
print("-" * 30)

client.close()