#!/usr/bin/python3

import ipaddress, fileinput

num = 0

for line in fileinput.input():
        ips = line.split("-")
        try:
                num = num + int(ipaddress.IPv4Address(str(ips[1][:-1]))) - int(ipaddress.IPv4Address(str(ips[0]))) + 1
        except (IndexError):
                print (ips)

print (num)
