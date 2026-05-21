import json
from napalm import get_network_driver

bgplist = ['192.168.42.10', '192.168.42.11']

# Move this outside the loop; you only need to define the driver type once
driver = get_network_driver('ios')

for ipaddr in bgplist:
    # Removed the '*' to fix the TypeError
    print('Getting BGP neighbors for {}'.format(ipaddr))
    
    device = driver(ipaddr, 'bryan', 'bryan')
    device.open()

    bgp_neighbors = device.get_bgp_neighbors()
    print(json.dumps(bgp_neighbors, indent=4))

    device.close()