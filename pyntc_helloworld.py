import json
from pyntc import ntc_device as NTC
DEVICES = ['192.168.42.10', '192.168.42.11']
CREDENTIALS = {'username': 'bryan', 'password': 'bryan'}

for ip in DEVICES:
    print(f"\n--- Connecting to {ip} ---")
    device = NTC(host=ip, username=CREDENTIALS['username'], password=CREDENTIALS['password'], device_type='cisco_ios_ssh')
    device.open()
    facts = device.facts()
    print(json.dumps(facts, indent=4))
    device.close()