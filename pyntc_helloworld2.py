import json
from pyntc import ntc_device as NTC

DEVICES = ['192.168.42.10', '192.168.42.11']
CREDENTIALS = {'username': 'bryan', 'password': 'bryan'}

for ip in DEVICES:
    print(f"\n--- Connecting to {ip} ---")
    device = NTC(host=ip, username=CREDENTIALS['username'], password=CREDENTIALS['password'], device_type='cisco_ios_ssh')
    device.open()
    print(f"Hostname: {device.hostname}")
    print(f"OS Version: {device.os_version}")
    print(f"Serial: {device.serial_number}")
    print(f"Model: {device.model}")
    device.close()