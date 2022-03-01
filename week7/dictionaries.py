#!/usr/bin/env python3

servers = { 'server1.testlab.com' : '192.168.1.10',
            'server2.testlab.com' : '192.168.1.11',
            'server3.testlab.com' : '192.168.1.12',
            'server4.testlab.com' : '192.168.1.13',
            'server5.testlab.com' : '192.168.1.14',
            'server6.testlab.com' : '192.168.1.15',
            'server7.testlab.com' : '192.168.1.16',
            'server8.testlab.com' : '192.168.1.15'
}

print(f"{servers.keys()}")
print(f"{servers.values()}")
print(f"{servers.items()}")
print(f"server2.testlab.com" in servers)
print(f"server10.testlab.com" in servers)