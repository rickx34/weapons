#!/usr/bin/env python3

#TODO: ADD color, multithreading

import socket
import argparse

def scan_open_ports(hostname):
    pass

def scan_port(hostname, port):
    print(hostname)
    try:
        serversocket.connect((hostname, port))
        print("{}\t\t[ OPEN ]".format(port))
    except:
        print("{}\t\t[ CLOSED ]".format(port))

def scan_common(hostname):
    pass
    
if __name__ == "__main__":
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    parser = argparse.ArgumentParser(description='Port Scanner')
    parser.add_argument('hostname', help='The host to scan')
    parser.add_argument('--all', nargs='?', help='scan all ports')

    args = parser.parse_args()
    scan_port("192.168.20.5", 1000)