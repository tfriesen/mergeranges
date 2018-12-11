#!/usr/bin/env python

import sys
import struct

def ip_sort_key(a):
    ''.join(("%03d" * 4) % tuple(a))

def int2ip(ip):
    return ".".join([str(ord(c)) for c in struct.pack(">L", ip)])

def ip2int(ip):
    return struct.unpack(">L", ''.join([chr(int(c)) for c in ip.strip().split(".")]))[0]


class Range:
    startip = 0
    endip = 0

    def __init__(self, sip, eip):
        self.startip = sip
        self.endip = eip

    def __init__(self, range):
        data = range.split("-")
        self.startip = ip2int(data[0])
        self.endip = self.startip
        if len(data) == 2:
            self.endip = ip2int(data[1])

    def __str__(self):
        return int2ip(self.startip) + "-" + int2ip(self.endip)

    def __gt__(self, range2):
        return self.startip > range2.startip

    def __eq__(self, range2):
        return self.startip == range2.startip and self.endip == range2.endip

    def __lt__(self, range2):
        return self.startip < range2.startip

    def __len__(self):
        return self.endip-self.startip +1

    def isAdjacent(self, range2):
        return (self.startip - range2.endip == 1) or (range2.startip - self.endip == 1)

    def contains(self, ip):
        return self.startip <= ip and self.endip >= ip

    def merge(self, range2):
        if self.isAdjacent(range2) or self.contains(range2.startip) or self.contains(range2.endip):
            if self.startip > range2.startip:
                self.startip = range2.startip
            if self.endip < range2.endip:
                self.endip = range2.endip
            return True
        return False



ranges = dict()

for l in sys.stdin:
    newrange = Range(l)
    wasMerged = False
    for r in ranges.itervalues():
        wasMerged = r.merge(newrange)
        if wasMerged:
            break
    if not wasMerged:
        ranges[newrange.startip] = newrange


#ranges2 = ranges.values().sort()
#print ranges.values()
#print ranges2
#for r in ranges2:
#    print r


for key in sorted(ranges.iterkeys()):
    print str(ranges[key])
