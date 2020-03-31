import json
import random
import math

with open(r'C:\Users\ksh04\Desktop\project\Python\MyBot2020\bot.json', encoding='utf-8', mode='r') as json_file:
    json_data = json.load(json_file)    
json_data['price'] = str(math.floor(int(json_data['price']) * random.randrange(80, 120) / 100))
with open(r'C:\Users\ksh04\Desktop\project\Python\MyBot2020\bot.json', encoding='utf-8', mode='w') as json_file:   
    json.dump(json_data, json_file, indent=4)