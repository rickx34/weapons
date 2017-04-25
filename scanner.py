#!/usr/bin/env python3

import argparse
import socket
import sys
from threading import Thread, Semaphore


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

COMMON_PORTS = [5,7,9,11,13,17,18,19,20,21,22,23,25,37,39,42,43,49,50,53,63,67,68,69,70,71,72,73,73,79,80,88,95,101,102,105,107,109,110,111,113,115,117,119,123,137,138,139,143,161,162,163,164,174,177,178,179,191,194,199,201,202,204,206,209,210,213,220,245,347,363,369,370,372,389,427,434,435,443,444,445,464,468,487,488,496,500,535,538,546,547,554,563,565,587,610,611,612,631,636,674,694,749,750,765,767,873,992,993,994,995,1080]

UNIX_PORTS = [512,512,513,513,514,514,515,517,518,519,520,520,521,525,526,530,531,532,533,540,543,544,548,556]

print_lock = Semaphore(value=1)

def scan_open_ports(hostname):
    pass

def scan_port(hostname, port):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        serversocket.connect((hostname, port))
        serversocket.send(b"Hello\r\n")
        data = serversocket.recv(100)
        service = data.rstrip().decode('utf-8')
        print_lock.acquire()
        print(bcolors.OKGREEN, "{}\t\t[ OPEN ]\t{}".format(port, service), bcolors.ENDC)
    except KeyboardInterrupt:
        sys.exit(1)
    except:
        if args.ports or args.verbose:
            print_lock.acquire()
            print(bcolors.FAIL, "{}\t\t[ CLOSED ]".format(port), bcolors.ENDC)
    finally:
        print_lock.release()
        serversocket.close()

def scan_common(hostname):
    for port in COMMON_PORTS:
        t = Thread(target=scan_port, args=(hostname, port))
        t.start()

def scan_all(hostname):
    for port in range(1, 65536):
        t = Thread(target=scan_port, args=(hostname, port))
        t.start()
    
if __name__ == "__main__":
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    parser = argparse.ArgumentParser(description='Port Scanner')
    # arg group to have either -a OR -p
    group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('hostname', help='The host to scan')
    parser.add_argument('-v', '--verbose', help='More verbose output', action='store_true')

    group.add_argument('-a', '--all', help='scan all ports (WARNING: may take a long time...)', dest='all', action='store_true')
    group.add_argument('-c', '--common', help='scan common ports', dest='common', action='store_true')
    group.add_argument('-p', help='port(s) to scan', nargs='+', dest='ports', metavar='port', type=int)

    args = parser.parse_args()
    print(args.hostname)
    if args.common:
        print("Scanning Common ports...")
        scan_common(args.hostname)
    elif args.ports:
        print("Scanning port(s)", args.ports)
        for port in args.ports:
            scan_port(args.hostname, port)
    elif args.all:
        scan_all(args.hostname)
