from netmiko import ConnectHandler

csw1 ={
    "device_type": "cisco_ios",
    "host": "192.168.42.30",
    "username": "bryan",
    "password": "bryan"
}

csw2 ={
    "device_type": "cisco_ios",
    "host": "192.168.42.31",
    "username": "bryan",
    "password": "bryan"
}

accsw1 ={
    "device_type": "cisco_ios",
    "host": "192.168.42.32",
    "username": "bryan",
    "password": "bryan"
}

accsw2 ={
    "device_type": "cisco_ios",
    "host": "192.168.42.33",
    "username": "bryan",
    "password": "bryan"
}


accsw3 ={
    "device_type": "cisco_ios",
    "host": "192.168.42.34",
    "username": "bryan",
    "password": "bryan"
}

with open("switch_configs.txt") as f:
    lines = f.read().splitlines()
    print(lines)
    
    all_switches = [csw1, csw2, accsw1, accsw2, accsw3]
    
for device in all_switches:
    net_connect = ConnectHandler(**device, timeout=60, banner_timeout=30, auth_timeout=30)
    output = net_connect.send_config_set(lines, read_timeout=60)
    print(output)

