# from distutils.log import error
from mcstatus import JavaServer
import os
import math
import threading
import time
import sys
import btl
import shutil

def helpmsg():
    help_message = f'''
    Usage: python {sys.argv[0]} [Input] [Output] [Threads]

    Input: Name of input file with server IPs (Generate me with masscan)

    Output: Where to save server IPs

    Threads: Number of threads

    '''
    print(help_message)
    sys.exit()

if not os.path.exists(sys.argv[1]):
    helpmsg()

if not os.path.isfile(sys.argv[1]):
    helpmsg()

try:
    inputfile = open(sys.argv[1], 'r').readlines()

    outputfile = sys.argv[2]

    threads = int(sys.argv[3])
except:
    helpmsg()

inputfile.remove(inputfile[-1])
inputfile.remove(inputfile[0])

if threads > len(inputfile):
    threads=len(inputfile)
    print(f'More threads than IPs. Defaulting number of threads to {threads}.')

def parse_ip(ip):
    return ip.split(' ')[3]+':25565'

def distribute_ips(ips, threads):
    chunk_size=math.ceil(len(ips)/threads)
    chunks = [ips[x:x+chunk_size] for x in range(0, len(ips), chunk_size)]
    return chunks

# global message
# global iplist

message = ''
iplist = ''

def run(*args):
    global message
    global iplist
    # print('Starting')
    raw_ip_list=args
    # print(args)
    logger = btl.Logger('=', 30)
    # print(message)
    for raw_ip in raw_ip_list:
        ip = parse_ip(raw_ip.strip())
        # print(f'Scanning {ip}')
        try:
            server = JavaServer.lookup(ip)
            status = server.status()
            
            message += logger.entry({
                'IP': ip,
                'Version': status.version.name,
                'MOTD': status.description,
                'Players Online': f'{status.players.online}/{status.players.max}'
            })
            # with open(str(id)+'ip.txt', 'a+') as file:
            #     file.write(ip+'\n')
            iplist += ip+'\n'
            if status.players.online > 0:
                print(f'Server {ip} has {status.players.online}/{status.players.max} players and is ready to raid.')
        except Exception as exc:
            # print(exc)
            # print('Failure')
            continue

dist_ips = distribute_ips(inputfile, threads)

thr=[]

for i in range(threads):
    # print(i)
    t = threading.Thread(target=run, args=(dist_ips[i]))
    thr.append(t)

for x in thr:
    # print(x)
    x.start()

for x in thr:
    # print(x)
    x.join()

with open(str(outputfile), 'w+', errors='ignore') as of:
    of.write(message)

with open('ip'+str(outputfile), 'w+') as of:
    of.write(iplist)

