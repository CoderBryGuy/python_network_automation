from netmiko import ConnectHandler

sw1 ={
    "device_type": "cisco_ios",
    "host": "192.168.122.11",
    "username": "bryan",
    "password": "bryan"
}

sw2 ={
    "device_type": "cisco_ios",
    "host": "192.168.122.12",
    "username": "bryan",
    "password": "bryan"
}

sw3 ={
    "device_type": "cisco_ios",
    "host": "192.168.122.13",
    "username": "bryan",
    "password": "bryan"
}

all_switches = [sw1, sw2, sw3]

for switch in all_switches:
    net_connect = ConnectHandler(**switch)
    for n in range(2, 21):
       print(f"Configuring VLAN {n} on {switch['host']}")
       config_commands = [f"vlan {n}", f"name Python_VLAN{n}"]
       output = net_connect.send_config_set(config_commands)
       print(output)