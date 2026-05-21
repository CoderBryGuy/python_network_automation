import json
from napalm import get_network_driver
driver = get_network_driver('ios')
switch2 = driver('192.168.42.10', 'bryan', 'bryan')
switch2.open()

facts = switch2.get_facts() 

ios_facts = json.dumps(facts, indent=4)
print(ios_facts)    

# print(f"Model: {facts['model']}")
# print(f"Hostname: {facts['hostname']}")
# print(f"OS Version: {facts['os_version']}")
# print(f"Serial Number: {facts['serial_number']}")
# print(f"Interface List: {facts['interface_list']}")