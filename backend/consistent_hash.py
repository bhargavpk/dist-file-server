import hash

# IP addresses of data-storing servers
storage_servers = [
    '10.10.10.1',
    '10.10.10.2',
    '10.10.10.3',
    '10.10.10.4'
]

storage_server_hashes = []


for ip in storage_servers:
    server_hash = hash.hashStrToNum(hash.hashStrToSha256(ip))
    storage_server_hashes.append([server_hash, ip])

storage_server_hashes.sort()

# Get IP address of approprite server for hash key
def getServer(key, servers):
    server_ip = servers[-1][1]
    for i in range(len(servers)):
        if servers[i][0] > key:
            server_ip = servers[i-1][1]
            break
    return server_ip




    
