import socket
import os 


def main():
    server_socket = socket.socket()
    server_socket.bind(("0.0.0.0", 8820))
    server_socket.listen()
    print("Server is up and running")

    (client_socket, client_address) = server_socket.accept()
    print("Client connected")

    data1 = client_socket.recv(1024).decode()
    parts=data1.split("@")
    action = parts[0]
    if action == "push":
        filename = parts[1]
        file_content = parts[2]
        with open(filename, "w") as f:
            f.write(file_content)
        with open('server_files', "a") as f:
            f.write(filename + "\n")
        reply = "the file has been pushed"
    if action == "pull":
        filename = parts[1]
        with open('server_files', "r") as f:
            file_list = f.read().splitlines()
        if filename in file_list and os.path.exists(filename):
            with open(filename, "r") as f:
                reply = f.read()
        else:
            reply = "The file doesn't exist in our database"
    if action == "delete":
        with open('server_files', 'w') as f:
            f.write("")
        reply = "the file content has been cleared"    

    client_socket.send(reply.encode())

    client_socket.close()
    server_socket.close()


if __name__ == '__main__':
    main()






