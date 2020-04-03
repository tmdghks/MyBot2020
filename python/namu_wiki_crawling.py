import requests
from bs4 import BeautifulSoup
import json

json_path = 'json_path'
r = requests.get("https://namu.wiki/w/%ED%8B%80:%EB%A6%AC%EA%B7%B8%20%EC%98%A4%EB%B8%8C%20%EB%A0%88%EC%A0%84%EB%93%9C/%EC%B1%94%ED%94%BC%EC%96%B8")
soup = BeautifulSoup(r.content, 'html.parser')
img_list = soup.find_all('img',{'class':'wiki-image'})[2:150]

with open(json_path, mode = 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    champions_list = json_data['league_champions_list']
    for img, champion in zip(img_list, champions_list):
        img_src = "https:" + img['src']
        try:
            json_data['league_champions_dict'][champion]['image'] = img_src
        except:
            json_data['league_champions_dict'][champion] = {}
            json_data['league_champions_dict'][champion]['image'] = img_src
        print(img_src)
with open(json_path, mode = 'w') as json_file:
    json.dump(json_data, json_file, indent=4, ensure_ascii=False)