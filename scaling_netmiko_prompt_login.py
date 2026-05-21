#!/usr/bin/env python3
from netmiko import ConnectHandler
from getpass import getpass

# 1. Fixed for Python 3 input and getpass import
username = input('Enter your SSH username: ')
password = getpass('Enter your SSH password: ')

# Read commands from file
with open('cmd_file.txt') as f:
    cmd_list = f.read().splitlines()
    
# Read device IPs from file
with open('device_file.txt') as f:
    device_list = f.read().splitlines()

# Loop through each device IP
for ip_address_of_device in device_list:
    print('\nConnecting to device: ' + ip_address_of_device)   
    
    # 2. Dynamic credentials passed into the dictionary
    ios_device = {
        'device_type': 'cisco_ios',
        'host': ip_address_of_device,
        'username': username,
        'password': password,
    }

    # 3. Indented the connection logic inside the loop so it touches every device
    try:
        with ConnectHandler(**ios_device) as net_connect:
            # Loop through the list of commands for this device
            for cmd in cmd_list:
                print(f"Running command: {cmd}")
                output = net_connect.send_command(cmd)
                print(output)
    except Exception as e:
        print(f"Failed to connect to {ip_address_of_device}: {e}")