import json
from napalm import get_network_driver
driver = get_network_driver('ios')
switch2 = driver('192.168.42.10', 'bryan', 'bryan')
switch2.open()

# facts = switch2.get_mac_address_table()
# facts = switch2.get_arp_table()
facts = switch2.ping('google.com', source='Vlan1', count=5)

ios_facts = json.dumps(facts, indent=4)
print(ios_facts)    

