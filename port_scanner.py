import socket
import argparse
from contextlib import closing

def check_socket(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            print ("Port is open")
            return 1
        else:
            print ("Port is not open")
            return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A Port Scanner to Scan the host")
    print("Usage: <python3> <filename> <host>")
    parser.add_argument('host', nargs="?", help="Host to perform stress test on")
    args = parser.parse_args()

    final_port = int(input("Enter the port you want to search to: "))

    for socket_count in range(801,final_port):
        print('---------------------------')
        print (socket_count)
        value = check_socket(args.host,socket_count)
        if value == 1:
            open_port = socket_count
            break
        if value == 0:
            continue
