import telnetlib

HOST = "192.168.122.20"
PORT = 23

tn = telnetlib.Telnet(HOST, PORT, timeout=10)
tn.read_until(b"Username: ", timeout=5)
tn.write(b"bryan\n")
tn.read_until(b"Password: ", timeout=5)
tn.write(b"bryan\n")
tn.read_until(b"\r\nR1#", timeout=5)

tn.write(b"configure terminal\n")
tn.read_until(b"(config)#", timeout=5)

# Loopback 1
tn.write(b"int loop 1\n")
tn.read_until(b"(config-if)#", timeout=5)
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.read_until(b"(config-if)#", timeout=5)
tn.write(b"exit\n")
tn.read_until(b"(config)#", timeout=5)

# Loopback 2
tn.write(b"int loop 2\n")
tn.read_until(b"(config-if)#", timeout=5)
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")
tn.read_until(b"(config-if)#", timeout=5)
tn.write(b"exit\n")
tn.read_until(b"(config)#", timeout=5)

# OSPF
tn.write(b"router ospf 1\n")
tn.read_until(b"(config-router)#", timeout=5)
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
tn.read_until(b"(config-router)#", timeout=5)

tn.write(b"end\n")
output = tn.read_until(b"\r\nR1#", timeout=5)
print(output.decode())

tn.close()