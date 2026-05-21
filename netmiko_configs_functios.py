from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException
import time

csw1   = {"device_type": "cisco_ios", "host": "192.168.42.30", "username": "bryan", "password": "bryan"}
csw2   = {"device_type": "cisco_ios", "host": "192.168.42.31", "username": "bryan", "password": "bryan"}
accsw1 = {"device_type": "cisco_ios", "host": "192.168.42.32", "username": "bryan", "password": "bryan"}
accsw2 = {"device_type": "cisco_ios", "host": "192.168.42.33", "username": "bryan", "password": "bryan"}
accsw3 = {"device_type": "cisco_ios", "host": "192.168.42.34", "username": "bryan", "password": "bryan"}


def push_config(devices, config_file, delay=5):
    with open(config_file) as f:
        lines = f.read().splitlines()

    print(f"Loaded {len(lines)} config lines\n")

    for device in devices:
        host = device["host"]
        try:
            print(f"Connecting to {host}...")
            with ConnectHandler(**device, timeout=60, banner_timeout=30, auth_timeout=30) as net_connect:
                output = net_connect.send_config_set(lines, read_timeout=60)
                print(f"[{host}] Output:\n{output}\n")
            print(f"[{host}] Done.\n")

        except NetmikoTimeoutException:
            print(f"[{host}] ERROR: Connection timed out.\n")
        except NetmikoAuthenticationException:
            print(f"[{host}] ERROR: Authentication failed.\n")
        except Exception as e:
            print(f"[{host}] ERROR: {e}\n")

        time.sleep(delay)


# --- acc3 -> acc2 -> acc1, then csw2 -> csw1 ---
push_config([accsw3, accsw2, accsw1], "access_config.txt")
push_config([csw2, csw1],             "core_config.txt")