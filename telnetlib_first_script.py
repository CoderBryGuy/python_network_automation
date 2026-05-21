import telnetlib

HOST = "192.168.42.20"
PORT = 23

tn = telnetlib.Telnet(HOST, PORT)

tn.read_until(b"Username: ")
tn.write(b"bryan\n")

tn.read_until(b"Password: ")
tn.write(b"bryan\n")           # your secret password

tn.read_until(b"# ")           # lands directly at priv 15 prompt
tn.write(b"configure terminal\n")

tn.read_until(b"(config)# ")
tn.write(b"int loop 1\n")

tn.read_until(b"(config-if)# ")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")

tn.read_until(b"(config-if)# ")
tn.write(b"end\n")

output = tn.read_until(b"# ")
print(output.decode())

tn.write(b"exit\n")
tn.close()