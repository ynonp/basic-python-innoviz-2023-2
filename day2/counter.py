def count(things):
    counter = {}
    for item in things:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return counter


count(['a', 'a', 'a', 'b', 'b', 'c']) == {'a': 3, 'b': 2, 'c': 1}
print(count(['a', 'a', 'a', 'b', 'b', 'c']))


os = {
    "172.2.1.1": "Red Hat",
    "172.2.1.2": "Ubuntu",
    "172.2.1.3": "Windows",
    "192.168.2.1": "Kali",
    "192.168.2.3": "Kali",
    "192.168.2.4": "Kali"
    }

print(count(os.values()))

only_kali = {
    ip: os
    for ip, os in os.items()
    if os == "Kali"
}
print(only_kali)

