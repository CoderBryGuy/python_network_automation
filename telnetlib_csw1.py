import telnetlib
import time

HOST = "192.168.42.30"
PORT = 23
TIMEOUT = 10

tn = telnetlib.Telnet(HOST, PORT, TIMEOUT)

# Wait for username prompt
tn.read_until(b"Username: ", TIMEOUT)
tn.write(b"bryan\n")

# Wait for password prompt
tn.read_until(b"Password: ", TIMEOUT)
tn.write(b"bryan\n")

# Wait for privileged prompt (lands at priv 15 directly)
tn.read_until(b"#", TIMEOUT)
tn.write(b"configure terminal\n")

# Wait for config prompt
tn.read_until(b"(config)#", TIMEOUT)

# Create VLANs one at a time, waiting for prompt between each
vlans = [10, 20, 30, 40, 50]
for vlan in vlans:
    tn.write(f"vlan {vlan}\n".encode())
    tn.read_until(b"(config-vlan)#", TIMEOUT)
    tn.write(b"exit\n")
    tn.read_until(b"(config)#", TIMEOUT)

# Exit config mode
tn.write(b"end\n")
tn.read_until(b"#", TIMEOUT)

# Verify VLANs were created
tn.write(b"show vlan brief\n")
output = tn.read_until(b"#", TIMEOUT)
print(output.decode())

tn.write(b"exit\n")
tn.close()