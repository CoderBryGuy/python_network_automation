import json
from pyntc import ntc_device as NTC

DEVICES = ['192.168.42.10', '192.168.42.11']
CREDENTIALS = {'username': 'bryan', 'password': 'bryan'}

for ip in DEVICES:
    print(f"\n--- Connecting to {ip} ---")
    # Note: ensure 'cisco_ios_ssh' is correct for your GNS3 images
    device = NTC(host=ip, username=CREDENTIALS['username'], password=CREDENTIALS['password'], device_type='cisco_ios_ssh')
    device.open()
    
    print(f"Current Hostname: {device.hostname}")
    
    # Define the target name
    new_hostname = 'SW2' if ip == '192.168.42.10' else 'R1'
    
    print(f"Changing hostname to '{new_hostname}'...")
    
    # Use the config method to send the actual IOS command
    device.config(f"hostname {new_hostname}")
    
    # if ip == '192.168.42.11':
    #     print("Enabling OSPF Area 0 on all interfaces for R1...")
    #     device.config(['router ospf 1', 'network 0.0.0.0 255.255.255.255 area 0'])


if ip == '192.168.42.11':
        print("Updating OSPF configuration for R1...")
        # We enter the OSPF process, remove the 'all' statement, and add specific networks
        ospf_commands = [
            'router ospf 1',
            'no network 0.0.0.0 255.255.255.255 area 0',
            'network 10.1.1.0 0.0.0.255 area 0',
            'network 10.1.2.0 0.0.0.255 area 1'
        ]
        device.config(ospf_commands)
        print("OSPF updated: 10.1.1.0 (Area 0) and 10.1.2.0 (Area 1)")
    
    # Best practice: save the running-config to startup-config
    # device.save() 
    
print(f"Verified New Hostname: {device.hostname}")
device.close()