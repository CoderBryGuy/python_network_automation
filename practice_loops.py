#! /usr/bin/env python3
import telnetlib

HOST = "192.168.42.31"
PORT = 23
TIMEOUT = 10

tn = telnetlib.Telnet(HOST, PORT, TIMEOUT)

tn.read_until(b"Username: ", TIMEOUT)
tn.write(b"bryan\n")

tn.read_until(b"Password: ", TIMEOUT)
tn.write(b"bryan\n")

tn.read_until(b"#", TIMEOUT)
tn.write(b"configure terminal\n")
tn.read_until(b"(config)#", TIMEOUT)

for n in range(1, 10):
    tn.write(f"vlan {n}\n".encode())
    tn.read_until(b"(config-vlan)#", TIMEOUT)
    tn.write(f"name Python_VLAN_{n}\n".encode())
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