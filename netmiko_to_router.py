from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.42.30',
    'username': 'bryan',
    'password': 'bryan',
}

# Establish connection
net_connect = ConnectHandler(**iosv_l2)

# Send a show command
output = net_connect.send_command('show ip int brief')
print(output)

# Send configuration commands
config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print(output)

# Loop to create VLANs
for n in range(2, 21):
    print(f"Creating VLAN {n}")  # Using f-strings (standard in Python 3.6+)
    config_commands = [f'vlan {n}', f'name Python_VLAN {n}']
    output = net_connect.send_config_set(config_commands)
    print(output)

# Good practice to disconnect
net_connect.disconnect()
