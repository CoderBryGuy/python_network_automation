#!/usr/bin/env python3
from netmiko import ConnectHandler

with open('cmd_file.txt') as f:
    cmd_list = f.read().splitlines()
    
with open('device_file.txt') as f:
    device_list = f.read().splitlines()

for devices in device_list:
    print('Connecting to device: ' + devices)   
    ip_address_of_device = devices
    ios_device   = {
    'device_type': 'cisco_ios',
    'host': ip_address_of_device,
    'username': 'bryan',
    'password': 'bryan',
    }
    
    # Using "with" guarantees the connection closes even if the script crashes
    with ConnectHandler(**ios_device) as net_connect:
        output = net_connect.send_command('show ip int brief')
        print(output)