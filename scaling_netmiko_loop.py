#!/usr/bin/env python3
from netmiko import ConnectHandler

# 1. Read your single combined file
with open('cmd_file.txt') as f:
    cmd_list = f.read().splitlines()

# 2. Define keywords that indicate a configuration change
# (You can add more keywords here as you discover them)
CONFIG_KEYWORDS = ['ip', 'interface', 'vlan', 'router', 'line', 'crypto', 'username', 'hostname']

iov_l2_s1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.42.10',
    'username': 'bryan',
    'password': 'bryan',
}

all_devices = [iov_l2_s1]   

for device in all_devices:
    print(f"Connecting to device: {device['host']}")
    
    with ConnectHandler(**device) as net_connect:
        for cmd in cmd_list:
            # Clean up trailing spaces and convert to lowercase for comparison
            clean_cmd = cmd.strip().lower()
            
            # Skip empty lines
            if not clean_cmd:
                continue
                
            # Check if the first word of the command is in our config keywords list
            first_word = clean_cmd.split()[0]
            
            if first_word in CONFIG_KEYWORDS:
                print(f"\n--- [CONFIG MODE] Executing: {cmd} ---")
                # Netmiko handles 'conf t' and 'end' for you behind the scenes here
                output = net_connect.send_config_set([cmd])
                print(output)
            else:
                print(f"\n--- [EXEC MODE] Executing: {cmd} ---")
                output = net_connect.send_command(cmd)
                print(output)