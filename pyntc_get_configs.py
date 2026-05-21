import json
from pyntc import ntc_device as NTC
iosvl2 = NTC(host='192.168.42.10', username='bryan', password='bryan', device_type='cisco_ios_ssh')
iosvl2.open()

ios_running_config = iosvl2.running_config
print("\n--- Running Configuration ---")
print(ios_running_config)

host = iosvl2.hostname
print(f"\nHostname: {host}")    
saveoutput = open("switch_" + host + "_running_config.txt", "w")
saveoutput.write(ios_running_config)
saveoutput.close()
iosvl2.close()  