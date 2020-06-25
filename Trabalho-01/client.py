import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname("localhost")

port = 9999

#Conexào estabelecida
print("Conexão estabelecida")
c.connect((host, port))

#primeira mensagem
fm = c.recv(1024)
fm = str(fm.decode('utf-8'))

print(fm)

#segunda mensagem
sm = c.recv(1024)
sm = str(sm.decode('utf-8'))

print(sm)

#primeira resposta
r1 = input()
c.send(r1.encode('ascii'))

#terceira mensagem
tm = c.recv(1024)
tm = str(tm.decode('utf-8'))

print(tm)

#segunda resposta
r2 = input()
c.send(r2.encode('ascii'))

#quarta mensagem
ftm = c.recv(1024)
ftm = str(ftm.decode('utf-8'))

print(ftm)

#terceira resposta
r3 = input()
c.send(r3.encode('ascii'))

#quinta mensagem
ffm = c.recv(1024)
ffm = str(ffm.decode('utf-8'))

print(ffm)

#quarta resposta
r4 = input()
c.send(r4.encode('ascii'))

#Resposta Final
finalm = c.recv(2048)
finalm = str(finalm.decode('utf-8'))

print(finalm)

#repetir??
am = c.recv(1024)
am = str(am.decode('utf-8'))

print(am)

#segunda resposta
rr = input()
c.send(rr.encode('ascii'))

if rr == "S":
    i=0
elif rr == "N":
    c.close()
