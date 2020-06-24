import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname("localhost")

port = 9999

server.bind((host, port))

server.listen()

clientsocket,addr = server.accept()
print("Got a connection from %s"% str(addr))


initinfo = """Este programa serve para você verificar se o peso das crianças
(Entre 3 e 18 anos) estão corretos para a idade"""
clientsocket.send(initinfo.encode("utf-8"))
firstQuestion = "Digite o genero do seu Filho(a) (M/F): "
clientsocket.send(firstQuestion.encode("utf-8"))
clientsocket.recv(1024)
