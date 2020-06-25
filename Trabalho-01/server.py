import socket
import person

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname('localhost')

port = 9999

server.bind((host, port))

server.listen(1)

print("Iniciando Servidor...")
clientsocket,addr = server.accept()

print("Got a connection from %s"% str(addr))

i = 0

while True: 
    initinfo = """Este programa serve para você verificar se o peso das criança (Entre 3 e 18 anos) estão corretos para a idade"""
    clientsocket.send(initinfo.encode("utf-8"))


    firstQuestion = "Digite o gênero do(a) seu Filho(a) (M/F): "
    clientsocket.send(firstQuestion.encode("utf-8"))
    gen = clientsocket.recv(1024)
    gen = str(gen.decode('ascii'))

    secQuestion = "Digite a idade do(a) seu Filho(a): "
    clientsocket.send(secQuestion.encode('ascii'))
    ag = clientsocket.recv(1024)
    ag = int(ag.decode('ascii'))

    thirdQuestion = "Digite o peso do(a) seu Filho(a) (10.0): "
    clientsocket.send(thirdQuestion.encode('ascii'))
    weig = clientsocket.recv(1024)
    weig = float(weig.decode('ascii'))

    fourthQuestion = "Digite a altura do(a) seu Filho(a): "
    clientsocket.send(fourthQuestion.encode('ascii'))
    heig = clientsocket.recv(1024)
    heig = float(heig.decode('ascii'))

    res = person.person(gen, ag, weig, heig)

    result = str(res.resultado())

    print(result)

    clientsocket.send(result.encode('utf-8'))

    tryAgain = "Deseja fazer outra consulta? (S/N)"
    clientsocket.send(tryAgain.encode('utf-8'))
    resTry = clientsocket.recv(1024)
    resTry = str(resTry.decode('ascii'))

    if resTry == "S":
        i = 0
    elif resTry == "N":
        i = 10
        clientsocket.close()





