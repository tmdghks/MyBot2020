import discord
import requests
import time
import random
import json

token = "token"
riot_api_key = 'api_key'
dinner_list = []
img_list = []

def get_rank(summoner_name: str):
    embed_color = 0
    try:
        summoner_id = requests.get('https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summoner_name + '?api_key=' + riot_api_key).json()['id']
        summoner_name = requests.get('https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summoner_name + '?api_key=' + riot_api_key).json()['name']
    except:
        embed = discord.Embed(
            title = summoner_name + '의 정보가 존재하지 않습니다.',
            color = 0xFF0000
        )
        return embed

    try:
        summoner_league_data = requests.get('https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/' + summoner_id + '?api_key=' + riot_api_key).json()[0]
        summoner_tier = summoner_league_data['tier']
        summoner_rank = summoner_league_data['tier'] + ' ' + summoner_league_data['rank']
        summoner_lp = summoner_league_data['leaguePoints']
    except:
        embed = discord.Embed(
            title = summoner_name + '의 랭크는 언랭입니다.',
            color = 0xFF0000
        )
        return embed
        
    if summoner_tier == 'IRON':
        embed_color = 0x3D3344
    elif summoner_tier == 'BRONZE':
        embed_color = 0x593833
    elif summoner_tier == 'SILVER':
        embed_color = 0x595F5F
    elif summoner_tier == 'GOLD':
        embed_color = 0xAB9F65
    elif summoner_tier == 'PLATINUM':
        embed_color = 0x79B28F
    elif summoner_tier == 'DIAMOND':
        embed_color = 0x7986B0
    elif summoner_tier == 'MASTER':
        embed_color = 0xE784F0
    elif summoner_tier == 'GRANDMASTER':
        embed_color = 0xFFA8A9
    elif summoner_tier == 'CHALLENGER':
        embed_color = 0xA8CBCF
    embed = discord.Embed(
        title = summoner_name + '의 정보',
        color = embed_color
    )
    embed.add_field(name= '티어', value= summoner_rank)
    embed.add_field(name= 'LP', value= summoner_lp)
    return embed

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as ', self.user)
        game = discord.Game("League of Legends")
        await client.change_presence(status=discord.Status.idle, activity=game)

    async def on_message(self, message):
        #don't response to ourselves
        print('메시지 작성자:', str(message.author), '메시지 내용:', str(message.content))
        if message.author == self.user:
            return
        
        if str(message.author).startswith('국지호') or str(message.author).startswith('dlrbdks'):
            tmp = random.randrange(0, 100)
            if tmp < 10:
                await message.channel.send(embed=discord.Embed(
                    title = str(message.author) + " 디코 그만하고 공부해라",
                    color = 0xFF0000
                ))

        if message.content == 'ping':
            await message.channel.send('pong')

        if message.content.startswith('!티어'):
            message_written = message.content.split()
            summoner_name = message_written[1:]
            summoner_name = " ".join(summoner_name)
            await message.channel.send(embed= get_rank(summoner_name))
            
        if message.content.startswith('!시간'):
            embed = discord.Embed(
                title = time.strftime('%c', time.localtime(time.time())),
                color = 0xFFFFFF    
            )
            await message.channel.send(embed=embed)

        if message.content.startswith('!아침'):
            with open(r'project_path\LeagueBot\dinner.json', encoding='utf-8') as json_file:
                json_data = json.load(json_file)
                dinner_list = json_data['word_list']
                array_index = random.randrange(0, len(dinner_list))
                embed = discord.Embed(
                    title = '오늘 아침은 ' + dinner_list[array_index] + '!',
                    color = random.randrange(0x000000, 0xFFFFFF)
                )
                await message.channel.send(embed=embed)

        if message.content.startswith('!강아지'):
            with open(r'project_path\LeagueBot\dinner.json', encoding='utf-8') as json_file:
                json_data = json.load(json_file)
                img_list = json_data['img_dog_list']
                array_index = random.randrange(0, len(img_list))
                await message.channel.send(img_list[array_index])
            

client = MyClient()
client.run(token)