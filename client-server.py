import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)
    print("Server is listening...")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024).decode()
        if not data: break
        print(f"Client: {data}")
        conn.send(input("Reply: ").encode())
    conn.close()
    server_socket.close()

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))
    while True:
        client_socket.send(input("Message: ").encode())
        data = client_socket.recv(1024).decode()
        if not data: break
        print(f"Server: {data}")
    client_socket.close()

if __name__ == "__main__":
    role = input("Server or Client? ").strip().lower()
    start_server() if role == "server" else start_client()


Explain