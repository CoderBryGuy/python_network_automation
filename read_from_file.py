#!/usr/bin/env python3
from getpass import getpass
import telnetlib

user = input("Enter username: ")
password = getpass("Enter password: ")

f = open('my_switches.txt', 'r')

for lin in f:
    print("Configuring switch " + lin.strip())

    HOST = str(lin.strip())
    PORT = 23
    TIMEOUT = 10
    tn = telnetlib.Telnet(HOST, PORT, TIMEOUT)

    tn.read_until(b"Username: ", TIMEOUT)
    tn.write((user + "\n").encode())
    tn.read_until(b"Password: ", TIMEOUT)
    tn.write((password + "\n").encode())
    tn.read_until(b"#", TIMEOUT)
    tn.write(b"configure terminal\n")
    tn.read_until(b"(config)#", TIMEOUT)

    for v in range(1, 11):
        tn.write(f"vlan {v}\n".encode())
        tn.read_until(b"(config-vlan)#", TIMEOUT)
        tn.write(f"name Python_VLAN_{v}\n".encode())
        tn.read_until(b"(config-vlan)#", TIMEOUT)
        tn.write(b"exit\n")
        tn.read_until(b"(config)#", TIMEOUT)

    tn.write(b"end\n")
    tn.read_until(b"#", TIMEOUT)
    tn.write(b"show vlan brief\n")
    output = tn.read_until(b"#", TIMEOUT)
    print(output.decode())
    tn.write(b"exit\n")
    tn.close()