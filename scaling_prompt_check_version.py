#!/usr/bin/env python3
from netmiko import ConnectHandler
from getpass import getpass
from netmiko import NetmikoAuthenticationException, NetmikoTimeoutException

# 1. Get credentials securely
username = input('Enter your SSH username: ')
password = getpass('Enter your SSH password: ')

# 2. Read distinct command sets from files
with open('switch_cmds_file.txt') as f:
    switch_cmds = f.read().splitlines()
    
with open('router_cmds_file.txt') as f:
    router_cmds = f.read().splitlines()
    
# 3. Read device IPs from file
with open('device_file.txt') as f:
    device_list = f.read().splitlines()

# 4. Keywords that belong to Configuration Mode
CONFIG_KEYWORDS = ['ip', 'interface', 'vlan', 'router', 'line', 'crypto', 'username', 'hostname', 'network', 'name']


# Loop through each device IP
for ip_address_of_device in device_list:
    if not ip_address_of_device.strip():
        continue
        
    print('\n=========================================')
    print(f'Connecting to device: {ip_address_of_device.strip()}')   
    print('=========================================')
    
    ios_device = {
        'device_type': 'cisco_ios',
        'host': ip_address_of_device.strip(),
        'username': username,
        'password': password,
    }

    try:
        with ConnectHandler(**ios_device) as net_connect:
            # Check software version to decide command list
            version_output = net_connect.send_command("show version")
            
            selected_cmd_list = []
            if 'vios_l2-ADVENTERPRISEK9-M' in version_output:
                print(">> Identified as a SWITCH. Loading switch commands.")
                selected_cmd_list = switch_cmds
            elif 'VIOS-ADVENTERPRISEK9-M' in version_output:
                print(">> Identified as a ROUTER. Loading router commands.")
                selected_cmd_list = router_cmds
            else:
                print(">> Unknown software version! Skipping configuration to be safe.")
                continue

            # Process the selected command list dynamically
            config_buffer = []
            for cmd in selected_cmd_list:
                clean_cmd = cmd.strip().lower()
                if not clean_cmd:
                    continue
                    
                first_word = clean_cmd.split()[0]
                
                # If it's a config command, save it to the buffer list
                if first_word in CONFIG_KEYWORDS:
                    config_buffer.append(cmd)
                else:
                    # If we hit a SHOW command, execute any stored configs first
                    if config_buffer:
                        print(f"\n--- Sending Config Block: {config_buffer} ---")
                        output = net_connect.send_config_set(config_buffer)
                        print(output)
                        config_buffer = [] # Reset the buffer
                    
                    print(f"\n--- [EXEC MODE] Executing: {cmd} ---")
                    output = net_connect.send_command(cmd)
                    print(output)
            
            # Flush any remaining configuration commands left at the bottom of the file
            if config_buffer:
                print(f"\n--- Sending Final Config Block: {config_buffer} ---")
                output = net_connect.send_config_set(config_buffer)
                print(output)
                            
    except NetmikoAuthenticationException:
        print(f"Authentication failed for {ip_address_of_device}. Please check your credentials.")
        continue  
    except NetmikoTimeoutException:
        print(f"Connection timed out for {ip_address_of_device}. The device may be unreachable.")
        continue  
    except EOFError:
        print(f"Unexpected EOF error while connecting to {ip_address_of_device}. The device may have closed the connection unexpectedly.")
        continue  
    except Exception as e:
        print(f"An unexpected error occurred while connecting to {ip_address_of_device}: {e}")  
        continue