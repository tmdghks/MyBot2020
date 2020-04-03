import requests
from bs4 import BeautifulSoup
import json

json_path = 'json_path'
r = requests.get("https://www.youtube.com/results?search_query=%ED%8E%98%EC%9D%B4%EC%BB%A4")
soup = BeautifulSoup(r.content, 'html.parser')
video_link = soup.find_all('a',{'class  ': 'yt-simple-endpoint style-scope ytd-video-renderer'})
print(video_link)