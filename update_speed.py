import sys
import json

if len(sys.argv) < 3:
    raise RuntimeError('python update_speed.py 韩伟鹏 59.00')

u_name = sys.argv[1]
u_speed = sys.argv[2]

with open('speed.json', 'r', encoding='utf-8') as f:
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

sorted_speed = sorted(name2speed.values(), key = lambda i: float(i['speed']))
accelerates = [25, 20, 15, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i, speed in enumerate(sorted_speed):
    speed['accelerate'] = str(accelerates[i]) if i < 15 else ''

with open('speed.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(sorted_speed, indent=4, ensure_ascii=False))
