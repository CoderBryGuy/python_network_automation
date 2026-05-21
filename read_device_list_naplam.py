from napalm import get_network_driver

DEVICES = ['192.168.42.10', '192.168.42.11']
CREDENTIALS = {'username': 'bryan', 'password': 'bryan'}
CONFIGS = ['acl1.cfg', 'ospf1.cfg']

driver = get_network_driver('ios')

def push_config(device, filename):
    device.load_merge_candidate(filename=filename)
    diffs = device.compare_config()
    if diffs:
        print(diffs)
        device.commit_config()
    else:
        print(f"No changes needed for {filename}")
        device.discard_config()

for ip in DEVICES:
    print(f"\n--- Connecting to {ip} ---")
    device = driver(ip, CREDENTIALS['username'], CREDENTIALS['password'])
    device.open()

    for config in CONFIGS:
        push_config(device, config)

    device.close()