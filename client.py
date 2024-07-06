import socket


my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("localhost", 8820))
PushPullDelete = input("enter push, pull or delete")
if PushPullDelete == "push":
    filename = input("enter files name to push ").strip()
    with open(filename, "r") as f:
        file_content = f.read()
    to_send = f"push@{filename}@{file_content}"
    my_socket.send(to_send.encode())
    D_ata = my_socket.recv(1024).decode()
    print(D_ata)
elif PushPullDelete == "pull":
    filename = input("enter files name to pull ").strip()
    to_send = f"pull@{filename}"
    my_socket.send(to_send.encode())
    D_ata = my_socket.recv(1024).decode()
    print(D_ata)
elif PushPullDelete == "delete":
    to_send = f"delete"
    my_socket.send(to_send.encode())
    D_ata = my_socket.recv(1024).decode()
    print(D_ata)
else:
    print("this function doesn't exist")
my_socket.close()

