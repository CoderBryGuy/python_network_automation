import json
from napalm import get_network_driver
driver = get_network_driver('ios')  
iosv2 = driver('192.168.42.10', 'bryan', 'bryan')
iosv2.open()

print("\n--- Get Config ---")
iosv2.load_merge_candidate(filename='ACL1.cfg')
iosv2.commit_config()
iosv2.close()