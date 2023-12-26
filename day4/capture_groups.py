"""
Sometimes we want to return part of the match
And for that we use capture groups
"""
import re
import io

demo_input = """
en19: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
status: active
nomatchen20 flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
options=400<CHANNEL_IO>
status: active
vmenet2: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
status: active
bridge102: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
vmenet3: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
ether ea:4d:c4:0f:83:60
media: autoselect
status: active
"""

for line in io.StringIO(demo_input):
    if m := re.search(r"^(([a-zA-Z]+)([0-9]+)):", line):
        print(m.group(1))






