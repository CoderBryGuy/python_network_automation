#! /usr/bin/env python3
import telnetlib

HOST = "192.168.42.30"
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

# VLANs with names
vlans = [
    (10,  "DATA"),
    (20,  "VOICE"),
    (30,  "MGMT"),
    (40,  "WLAN"),
    (50,  "GUEST"),
    (100, "SERVERS"),
    (101, "NATIVE"),
]

for vlan_id, vlan_name in vlans:
    tn.write(f"vlan {vlan_id}\n".encode())
    tn.read_until(b"(config-vlan)#", TIMEOUT)
    tn.write(f"name {vlan_name}\n".encode())
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

