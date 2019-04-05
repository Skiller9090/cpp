import socket
import urllib.request
import json
host = ""
port = 25565

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port,))
server.listen(1)


def findbestproxy(ssl,proxytype,timeout):
    if ssl == 1:
        ssl = "yes"
    else:
        ssl = "no"
    link = 'https://api.proxyscrape.com?request=displayproxies&proxytype='+proxytype+'&timeout='+timeout+'&format=json&anonymity=elite&ssl='+ssl+''
    response = urllib.request.urlopen(link)
    output = response.read().decode()
    output_2 = output.replace("\r","")
    dictionary = json.loads(output_2)
    bestproxy = 0
    bestspeed = dictionary[0]['timeout']

    for i in range(len(dictionary)):
        dictionary[i]['timeout']
        if dictionary[i]['timeout'] < bestspeed:
            bestspeed = dictionary[i]['timeout']
            bestproxy = i
    aspects = []
    for i in dictionary[bestproxy]:
        aspects.append(i)
    proxy_info = []
    for i in aspects:
        proxy_info.append(i+": "+str(dictionary[bestproxy][i]))
    proxy_info_string = "\n".join(proxy_info)
    return proxy_info_string
while True:
    con,addr = server.accept()
    variables = con.recv(4096).decode()
    variables = variables.split("\n")
    con.send(findbestproxy(int(variables[0]),variables[1],variables[2]).encode())
    con.close()
