os = {
    "172.2.1.1": "Red Hat",
    "172.2.1.2": "Ubuntu",
    "172.2.1.3": "Windows",
    "192.168.2.1": "Kali",
    }

ports = {
        "172.2.1.1": [80, 21],
        "172.2.1.2": [80, 22, 443],
        }

print(os["172.2.1.1"])

for key, value in os.items():
    print(f"ip = {key} is using {value}")

for ip, os in os.items():
    print(f"ip = {ip} is using {os}")

print(os.keys())
print(os.values())









