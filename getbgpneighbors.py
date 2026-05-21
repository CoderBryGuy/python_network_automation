import json
from napalm import get_network_driver
driver = get_network_driver('ios')
switch2 = driver(' 192.168.42.10', 'bryan', 'bryan')
switch2.open()

bgp_neighbors = switch2.get_bgp_neighbors()
print(json.dumps(bgp_neighbors,indent=4))

switch2.close()