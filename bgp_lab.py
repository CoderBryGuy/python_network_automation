import json
from napalm import get_network_driver
driver=get_network_driver('ios')
iovsrouter = driver('192.168.42.155', 'bryan', 'bryan')
iovsrouter.open() 

ios_output = iovsrouter.get_facts()
print(json.dumps(ios_output, indent=4))  

ios_output = iovsrouter.get_bgp_neighbors()
print(json.dumps(ios_output, indent=4))