#!/usr/bin/env python3
from getpass import getpass
import telnetlib

#ask for username and password
user = input("Enter username: ")
password = getpass("Enter password: ")

#open the file with the list of switches
f = open('my_switches.txt', 'r')

#telnet to each switch and get the running config, then save it to a file
for lin in f:
    print("Get running config from switch " + lin.strip())

    HOST = str(lin.strip())
    PORT = 23
    TIMEOUT = 10
    tn = telnetlib.Telnet(HOST, PORT, TIMEOUT)

    tn.read_until(b"Username: ", TIMEOUT)
    tn.write((user + "\n").encode())
    tn.read_until(b"Password: ", TIMEOUT)
    tn.write((password + "\n").encode())
    tn.read_until(b"#", TIMEOUT)
    tn.write(b"terminal length 0\n")
    tn.read_until(b"#", TIMEOUT)    
    tn.write(b"show run\n")

#display the output on the screen
    output = tn.read_until(b"#", TIMEOUT)
    print(output.decode())
    tn.write(b"exit\n")

#save the output to a file
    save_output = open("switch_" + HOST + ".txt", "w")
    save_output.write(output.decode())
    save_output.close()
    tn.close()