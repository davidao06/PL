import re

ips = ['Esta  ́e uma linha de lixo.','251.1.19.20','2001:0db8:0000:0000:0005:ff00:0042:8329','epl.di.uminho.pt 193.136.19.129']

regexIPv4 = r'^(25[0-5]\.|2[0-4]\d\.|1\d\d\.|\d\d\.|\d\.){3}(25[0-5]|2[0-4]\d|1\d\d|\d\d|\d)$'
regexIPv6 = r'^([\da-f]{1,4}:){7}[\da-f]{1,4}$'

for s in ips:
    v4 = re.search(regexIPv4,s)
    v6 = re.search(regexIPv6,s)
    if v4:
        print('IPv4:',v4.group())
    elif v6:
        print("IPv6:",v6.group())
    else:
        print("Erro")
