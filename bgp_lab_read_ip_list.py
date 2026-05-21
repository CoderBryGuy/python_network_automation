import json
from napalm import get_network_driver
from napalm.base.exceptions import ConnectionException

# Configuration
driver = get_network_driver('ios')
ip_file = 'bgp_lab_ips.txt'
username = 'bryan'
password = 'bryan'

# Open the file and read the IPs
try:
    with open(ip_file, 'r') as f:
        # .splitlines() removes the newline characters (\n) from each line
        devices = f.read().splitlines()
except FileNotFoundError:
    print(f"Error: {ip_file} not found.")
    devices = []

for ip in devices:
    # Clean up any accidental whitespace
    ip = ip.strip()
    if not ip:
        continue

    print(f"\n--- Connecting to {ip} ---")
    
    device = driver(ip, username, password)
    
    try:
        device.open()
        
        # Get Facts
        print(f"Fetching facts for {ip}...")
        facts = device.get_facts()
        print(json.dumps(facts, indent=4))
        
        # Get BGP Neighbors
        print(f"Fetching BGP neighbors for {ip}...")
        bgp_neighbors = device.get_bgp_neighbors()
        print(json.dumps(bgp_neighbors, indent=4))
        
        device.close()
        
    except ConnectionException:
        print(f"Could not connect to {ip}. Check routing or SSH config.")
    except Exception as e:
        print(f"An error occurred with {ip}: {e}")

print("\n--- Task Complete ---")