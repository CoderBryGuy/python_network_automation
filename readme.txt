# Network Automation Scripts

## Requirements
- Python 3.12 or earlier (telnetlib removed in 3.13)
- GNS3 with IOSv

## Setup
- Router IP: 192.168.42.x subnet
- Username: bryan / Password: bryan
- privilege 15 on vty lines

## Scripts
- `test.py` - debug/repr to read raw telnet bytes
- `pyscript_r1.py` - configures Loopback1 on R1 via Telnet

## Lessons Learned
- use repr() to see exact bytes coming from the router
- read_until() is just a byte string search, not smart
- match \r\nR1# not just R1# to avoid false matches