#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
#para acessa sys.argv[n]
#isso será usado para melhorar o programa
def modulo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 128
    elif num == 2:
        return 192
    elif num == 3:
        return 224
    elif num == 4:
        return 240
    elif num == 5:
        return 248
    elif num == 6:
        return 252
    elif num == 7:
        return 254
def usage():
    print "------------SYSNETWORK--------------"
    print "Usage : sysnet.py -i 192.168.0.14 -c /24"
    print "the program return to user the network, the broadcast"
    print "also the number of valids ips in the network"
def calcs(ip,cidr):
    ipext = ip.split(".")
    ncdr = 0
    if len(cidr) <= 1 or len(cidr)>3:
        usage()
    elif len(cidr)== 2:
        ncdr = int(cidr[1])
    else:
        ncdr = int(cidr[1]+cidr[2])
    cidrint = (ncdr/8)
    cidrmod = ncdr%8
    if cidrint == 4:
        print "you have a only host"
    elif cidrint == 3:
        o1 = ipext[0]
        o2 = ipext[1]
        o3 = ipext[2]
        o4 = "0"
        print "you network is %s"%(".".join([o1,o2,o3,o4]))
        print "you broadcast is %s"%(".".join([o1,o2,o3,"255"]))
        print "you have %s hosts"%(2**8 - 2)
    elif cidrint == 2:
        o1 = ipext[0]
        o2 = ipext[1]
        o3 = "0"
        o4 = "0"
        print "you network is %s"%(".".join([o1,o2,o3,o4]))
        print "you broadcast is %s"%(".".join([o1,o2,"255","255"]))
        print "you have %s hosts"%(2**16 - 2)
    elif cidrint == 1:
        o1 = ipext[0]
        o2 = "0"
        o3 = "0"
        o4 = "0"
        print "you network is %s"%(".".join([o1,o2,o3,o4]))
        print "you broadcast is %s"%(".".join([o1,"255","255","255"]))
        print "you have %s hosts"%(2**24 - 2)
    else:
        print "Isso non exciste!"
def main():
    if len(sys.argv) != 5:
        usage()
    else:
        calcs(sys.argv[2],sys.argv[4])
main()
    
