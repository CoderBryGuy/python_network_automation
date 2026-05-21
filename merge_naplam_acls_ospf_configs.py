import json
from napalm import get_network_driver
driver = get_network_driver('ios')  
iosv2 = driver('192.168.42.11', 'bryan', 'bryan')
iosv2.open()

print("\n--- Get Config ---")

iosv2.load_merge_candidate(filename='acl1.cfg')
diffs = iosv2.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosv2.commit_config()
else: 
    print("No changes needed.")
    iosv2.discard_config()
    
iosv2.load_merge_candidate(filename='ospf1.cfg')
diffs = iosv2.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosv2.commit_config()
else: 
    print("No OSPF changes needed.")
    iosv2.discard_config()
    
iosv2.close()