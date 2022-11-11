import socket
import threading


def server(conn_, addr_):
    while True:
        data = conn_.recv(1024)
        if not data or data == 'close':
            break
        conn_.send(data)
    conn_.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
    conn, addr = s.accept()
    task = threading.Thread(target=server, args=(conn, addr))
    task.start()
