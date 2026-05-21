#!/usr/bin/env python3
from netmiko import ConnectHandler

with open('cmd_file.txt') as f:
    cmd_list = f.read().splitlines()

iov_l2_s1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.42.10',
    'username': 'bryan',
    'password': 'bryan',
}

all_devices = [iov_l2_s1]   

# Using "with" guarantees the connection closes even if the script crashes
with ConnectHandler(**iov_l2_s1) as net_connect:
    output = net_connect.send_command('show ip int brief')
    print(output)