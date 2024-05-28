import json
import random

data = {
    "category": ["A", "B", "C", "D", "E"],
    "values": [random.randint(10, 100) for _ in range(5)]
}

with open('data.json', 'w') as f:
    json.dump(data, f)

print(data)