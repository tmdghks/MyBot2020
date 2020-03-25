import discord
import requests
import time
import random
import json
from bs4 import BeautifulSoup
import re

discord_token = "token"
riot_api_key = 'api_key'
dinner_list = []
img_list = []
study_bool = True
study_percent = 10


def get_rank(summoner_name: str):
    embed_color = 0
    try:
        summoner_id = requests.get('https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' +
                                   summoner_name + '?api_key=' + riot_api_key).json()['id']
        summoner_name = requests.get('https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/' +
                                     summoner_name + '?api_key=' + riot_api_key).json()['name']
    except:
        embed = discord.Embed(
            title=summoner_name + '의 정보가 존재하지 않습니다.',
            color=0xFF0000
        )
        return embed

    try:
        summoner_league_data = requests.get(
            'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/' + summoner_id + '?api_key=' + riot_api_key).json()[0]
        summoner_tier = summoner_league_data['tier']
        summoner_rank = summoner_league_data['tier'] + \
            ' ' + summoner_league_data['rank']
        summoner_lp = summoner_league_data['leaguePoints']
    except:
        embed = discord.Embed(
            title=summoner_name + '의 랭크는 언랭입니다.',
            color=0xFF0000
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
        title=summoner_name + '의 정보',
        color=embed_color
    )
    embed.add_field(name='티어', value=summoner_rank)
    embed.add_field(name='LP', value=summoner_lp)
    return embed


def get_corona_data():
    res = requests.get('https://www.coronanow.kr/')
    soup = BeautifulSoup(res.content, 'html.parser')

    tmp = soup.select(
        '#layoutSidenav_content > main > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div > div.card-body2')[0].get_text()
    tmp = tmp.replace(",", "")
    positive_number = re.findall("\d+", tmp)
    if len(positive_number) == 1:
        positive_number.append(str(0))

    tmp = soup.select(
        '#layoutSidenav_content > main > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div > div.card-body2')[0].get_text()
    tmp = tmp.replace(",", "")
    deaths_number = re.findall("\d+", tmp)
    if len(deaths_number) == 1:
        deaths_number.append(str(0))

    tmp = soup.select(
        '#layoutSidenav_content > main > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div > div.card-body2')[0].get_text()
    tmp = tmp.replace(",", "")
    recoveries_number = re.findall("\d+", tmp)
    if len(recoveries_number) == 1:
        recoveries_number.append(str(0))

    Corona_data = positive_number + recoveries_number + deaths_number

    return Corona_data


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as ', self.user)
        game = discord.Game("League of Legends")
        await client.change_presence(status=discord.Status.idle, activity=game)

    async def on_message(self, message):
        global study_bool
        global study_percent

        print('메시지 작성자:', str(message.author), '메시지 내용:', str(message.content))

        # don't response to ourselves
        if message.author == self.user:
            return

        if (str(message.author).startswith('국지호') or str(message.author).startswith('dlrbdks')) and study_bool == True:
            tmp = random.randrange(0, 100)
            if tmp < int(study_percent):
                await message.channel.send(embed=discord.Embed(
                    title=str(message.author) + " 디코 그만하고 공부해라",
                    color=0xFF0000
                ))

        if message.content == 'ping':
            await message.channel.send('pong')

        if message.content.startswith('!티어'):
            message_written = message.content.split()
            summoner_name = message_written[1:]
            summoner_name = " ".join(summoner_name)
            await message.channel.send(embed=get_rank(summoner_name))

        if message.content.startswith('!시간'):
            embed = discord.Embed(
                title=time.strftime('%c', time.localtime(time.time())),
                color=0xFFFFFF
            )
            await message.channel.send(embed=embed)

        if message.content.startswith('!아침'):
            with open(r'project_path\LeagueBot\dinner.json', encoding='utf-8') as json_file:
                json_data = json.load(json_file)
                dinner_list = json_data['word_list']
                array_index = random.randrange(0, len(dinner_list))
                embed = discord.Embed(
                    title='오늘 아침은 ' + dinner_list[array_index] + '!',
                    color=random.randrange(0x000000, 0xFFFFFF)
                )
                await message.channel.send(embed=embed)

        if message.content.startswith('!강아지'):
            with open(r'C:\Users\ksh04\Desktop\project\Python\MyBot2020\dinner.json', encoding='utf-8') as json_file:
                json_data = json.load(json_file)
                img_list = json_data['img_dog_list']
                array_index = random.randrange(0, len(img_list))
                await message.channel.send(img_list[array_index])

        if message.content.startswith('!계산'):  # 사칙연산 결과값을 구함 #made by 이규안
            Equation = ""
            message_written = message.content.split()
            print(message_written[1:])  # 디버그용
            for i in range(1, len(message_written)):
                Equation = Equation + str(message_written[i])
            try:
                result = str(eval(Equation))  # eval = 계산 가능한 문자열 계산해 int로 변경
                if result[-2:] == '.0':  # 숫자 뒤에 '.0'있을때 '.0'제거
                    Result = result[:-2]
                    embed = discord.Embed(
                        title='계산결과', color=random.randrange(0x000000, 0xFFFFFF))
                    embed.add_field(name=Equation, value=Result, inline=False)
                    await message.channel.send(embed=embed)
                else:  # 숫자 뒤 '.0'없을때 그대로 전송
                    embed = discord.Embed(
                        title='계산결과', color=random.randrange(0x000000, 0xFFFFFF))
                    embed.add_field(name=Equation, value=result, inline=False)
                    await message.channel.send(embed=embed)
            except:
                await message.channel.send(embed=discord.Embed(
                    title="수식이 잘못되었습니다.",
                    color=0xFF0000
                ))

        if message.content.startswith('!코로나'):
            corona_data = get_corona_data()
            embed = discord.Embed(
                title="국내 코로나 현황",
                color=0xFF0000
            )
            embed.add_field(name='확진자', value=str(corona_data[0]) + '명')
            embed.add_field(name='확진자 전일대비', value=str(
                corona_data[1]) + "명 증가")
            embed.add_field(name='회복자', value=str(corona_data[2]) + '명')
            embed.add_field(name='회복자 전일대비', value=str(
                corona_data[3]) + "명 증가")
            embed.add_field(name='사망자', value=str(corona_data[4]) + '명')
            embed.add_field(name='사망자 전일대비', value=str(
                corona_data[5]) + "명 증가")
            await message.channel.send(embed=embed)

        if message.content.startswith('!공부해라'):
            message_written = message.content.split()
            if str(message.author).startswith('tmdghks'):
                if message_written[1] == "켜라":
                    if study_bool == True:
                        await message.channel.send(embed=discord.Embed(
                            title="이미 켜져 있습니다.",
                            color=0x00FF00
                        ))
                    else:
                        await message.channel.send(embed=discord.Embed(
                            title="공부해라를 켰습니다.",
                            color=0xFF0000
                        ))
                        study_bool = True
                elif message_written[1] == "꺼라":
                    if study_bool == False:
                        await message.channel.send(embed=discord.Embed(
                            title="이미 꺼져 있습니다.",
                            color=0xFF0000
                        ))
                    else:
                        await message.channel.send(embed=discord.Embed(
                            title="공부해라를 껐습니다.",
                            color=0x00FF00
                        ))
                        study_bool = False
                try:
                    study_percent = message_written[2]
                except:
                    study_percent = 10
            else:
                await message.channel.send(embed=discord.Embed(
                    title=str(message.author) + ' 이 명령어를 사용할 권한이 없습니다.',
                    color=0xFF0000
                ))


client = MyClient()
client.run(discord_discord_token)
