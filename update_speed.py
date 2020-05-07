import sys
import json

if len(sys.argv) < 3:
    raise RuntimeError('python update_speed.py 韩伟鹏 59.00')

u_name = sys.argv[1]
u_speed = sys.argv[2]

with open('speed.json', 'r') as f:
    speeds = json.loads(f.read())

name2speed = dict()
for speed in speeds:
    name2speed[speed['car']] = speed

if u_name in name2speed:
    name2speed[u_name]['speed'] = u_speed
else:
    name2speed[u_name] = {
                "car": u_name,
                "BID": "",
                "Btitle": "",
                "hp": "",
                "hp_content": "",
                "Powertrain": "",
                "speed": u_speed,
                "mods": "0",
                "tyre": "大闪电",
                "temperature": "",
                "lv": "",
                "time": "",
                "accelerate": "",
                "limit": ""}

print (sorted(name2speed.values(), key = lambda i: float(i['speed'])) )

