import socket
def con():
    server_addr = input("What server do you want to connect to? ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_addr, 80))
    sock.send(b"GET / HTTP/1.1\r\nHost: " +
              bytes(server_addr, "utf8") +
              b"\r\nConnection: close\r\n\r\n")
    reply = sock.recv(10000)
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
    print(repr(reply))

def js():
    import json

    class Who:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    def encode_who(w):
        if isinstance(w, Who):
            return w.__dict__
        else:
            raise TypeError(w.__class__.__name__ + ' is not JSON serializable')

    some_man = Who('John Doe', 42)
    print(json.dumps(some_man, default=encode_who))
