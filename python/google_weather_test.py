import json
import random
import math

json_path = 'json_path'
with open(json_path, encoding='utf-8', mode='r') as json_file:
    json_data = json.load(json_file)    
json_data['price'] = str(math.floor(int(json_data['price']) * random.randrange(80, 120) / 100))
with open(json_path, encoding='utf-8', mode='w') as json_file:   
    json.dump(json_data, json_file, indent=4)