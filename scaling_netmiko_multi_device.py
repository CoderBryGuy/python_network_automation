#!/usr/bin/env python3
from netmiko import ConnectHandler

# 1. Read your commands and device IPs from files
with open('cmd_file.txt') as f:
    cmd_list = f.read().splitlines()
    
with open('device_file.txt') as f:
    device_list = f.read().splitlines()

# 2. Define keywords that indicate a configuration change
# Added 'network' here just in case!
CONFIG_KEYWORDS = ['ip', 'interface', 'vlan', 'router', 'line', 'crypto', 'username', 'hostname', 'network']

# 3. Dynamically build your list of device dictionaries
all_devices = []
for device_ip in device_list:
    # Skip any empty lines in your device file
    if not device_ip.strip():
        continue
    device = {
        'device_type': 'cisco_ios',
        'host': device_ip.strip(),
        'username': 'bryan',
        'password': 'bryan',
    }
    all_devices.append(device)

# 4. Loop through and configure every device
for device in all_devices:
    print(f"\n=========================================")
    print(f"Connecting to device: {device['host']}")
    print(f"=========================================")
    
    try:
        with ConnectHandler(**device) as net_connect:
            config_buffer = []
            
            for cmd in cmd_list:
                clean_cmd = cmd.strip().lower()
                if not clean_cmd:
                    continue
                    
                first_word = clean_cmd.split()[0]
                
                # If it's a config command, buffer it so they stay grouped together
                if first_word in CONFIG_KEYWORDS:
                    config_buffer.append(cmd)
                else:
                    # If we hit a SHOW command, execute any pending configs first
                    if config_buffer:
                        print(f"\n--- Sending Config Block: {config_buffer} ---")
                        output = net_connect.send_config_set(config_buffer)
                        print(output)
                        config_buffer = []  # Reset the buffer
                    
                    print(f"\n--- [EXEC MODE] Executing: {cmd} ---")
                    output = net_connect.send_command(cmd)
                    print(output)
            
            # Flush any remaining config lines left at the bottom of the file
            if config_buffer:
                print(f"\n--- Sending Final Config Block: {config_buffer} ---")
                output = net_connect.send_config_set(config_buffer)
                print(output)
                
    except Exception as e:
        print(f"CRITICAL: Failed to connect or run commands on {device['host']}: {e}")