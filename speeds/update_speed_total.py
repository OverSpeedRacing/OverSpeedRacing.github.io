import json
import sys

json_files = list()

for s in sys.argv:
    if s.endswith('.json'):
        json_files.append(s)

total_speeds = dict()
for fname in json_files:
    with open(fname, 'r', encoding='utf-8') as f:
        for new_speed in json.loads(f.read()):
            if new_speed['name'] not in total_speeds:
                total_speeds[new_speed['name']] = new_speed
            else:
                if float(new_speed['speed']) < float(total_speeds[new_speed['name']]['speed']):
                    total_speeds[new_speed['name']]['speed'] = new_speed['speed']
                    total_speeds[new_speed['name']]['hp_content'] = new_speed['hp_content']
                total_speeds[new_speed['name']]['accelerate'] = str(int(total_speeds[new_speed['name']]['accelerate']) + int(new_speed['accelerate']))


sorted_speed = sorted(total_speeds.values(), key = lambda i: float(i['accelerate']), reverse=True)


with open('speed_2020.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(sorted_speed, indent=4, ensure_ascii=False))
