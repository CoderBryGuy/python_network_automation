#!/usr/bin/env python3
from netmiko import ConnectHandler

with open('cmd_file.txt') as f:
    cmd_list = f.read().splitlines()

CONFIG_KEYWORDS = ['ip', 'interface', 'vlan', 'router', 'line', 'crypto', 'username', 'hostname', 'network']

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
        config_buffer = []
        
        for cmd in cmd_list:
            clean_cmd = cmd.strip().lower()
            if not clean_cmd:
                continue
                
            first_word = clean_cmd.split()[0]
            
            # If it's a config command, save it to our buffer to send together
            if first_word in CONFIG_KEYWORDS:
                config_buffer.append(cmd)
            else:
                # If we hit a SHOW command, flush any pending configs first
                if config_buffer:
                    print(f"\n--- Sending Config Block: {config_buffer} ---")
                    output = net_connect.send_config_set(config_buffer)
                    print(output)
                    config_buffer = [] # Clear the buffer
                
                print(f"\n--- [EXEC MODE] Executing: {cmd} ---")
                output = net_connect.send_command(cmd)
                print(output)
        
        # Flush any remaining config commands left at the end of the file
        if config_buffer:
            print(f"\n--- Sending Config Block: {config_buffer} ---")
            output = net_connect.send_config_set(config_buffer)
            print(output)