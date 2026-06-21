blacklisted_ips = [
    "192.168.1.10",
    "10.0.0.5",
    "172.16.1.100",
    "192.168.0.50"
]

ip = input("Enter an IP Address: ")

if ip in blacklisted_ips:
    print("IP Found in Blacklist")
else:
    print("IP Not Found")blacklist_checkers