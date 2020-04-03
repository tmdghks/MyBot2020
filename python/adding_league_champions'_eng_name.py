import json

json_path = 'json_path'
league_eng_name_list = ['Garen', 'Galio', 'Gangplank', 'Gragas', 'Graves', 'Gnar', 'Nami', 'Nasus', 'Nautilus', 'Nocuturne', 'Nunu', 'Nidalee', 'Neeko', 'Darius', 'Diana', 'Draven', 'Ryze', 'Rakan', 'Rammus', 'Lux', 'Rumble', 'Renekton', 'Leona', 'RekSai', 'Rengar', 'Lucian', 'Lulu', 'LeBlanc', 'LeeSin', 'Riven', 'Lissandra', 'MasterYi', 'Maokai', 'Malzahar', 'Malphite', 'Mordekaiser', 'Morgana', 'DrMundo', 'MissFortune', 'Bard', 'Varus', 'Vi', 'Veigar', 'Vayne', 'Velkoz', 'Volibear', 'Braum', 'Brand', 'Vladimir' , 'Blitzcrank', 'Viktor', 'Poppy', 'Sion', 'Sylas', 'Shaco', 'Senna', 'Sejuani', 'Sett', 'Sona', 'Soraka', 'Shen', 'Shyvana', 'Swain', 'Skarner', 'Sivir', 'XinZhao', 'Syndra', 'Singed', 'Thresh', 'Ahri', 'Amumu', 'AurelionSol', 'Ivern', 'Azir', 'Akali', 'Aatrox', 'Aphelios', 'Alistar', 'Annie', 'Anivia', 'Ashe', 'Yasuo', 'Ekko', 'Elise', 'Wukong', 'Ornn', 'Orianna', 'Olaf', 'Yorick', 'Udyr', 'Urgot', 'Warwick', 'Yuumi', 'Irelia', 'Evelynn', 'Ezreal', 'Illaoi', 'JarvanIV', 'Xayah', 'Zyra', 'Zac', 'Janna', 'Jax', 'Zed', 'Xerath', 'Jayce', 'Zoe', 'Ziggs', 'Jhin', 'Zilean', 'Jinx', 'ChoGath', 'Karma', 'Camille', 'Kassadin', 'Karthus', 'Cassiopeia', 'KaiSa', 'KhaZix', 'Katarina', 'Kalista', 'Kennen', 'Caitlyn', 'Kayn', 'Kayle', 'CogMaw', 'Corki', 'Quinn', 'Kled', 'Qiyana', 'Kindred', 'Taric', 'Talon', 'Taliyah', 'TahmKench', 'Trundle', 'Tristana', 'Tryndamere', 'TwistedFate', 'Twitch', 'Teemo', 'Pyke', 'Pantheon', 'Fiddlesticks', 'Fiora', 'Fizz', 'Heimerdinger', 'Hecarim']

with open(json_path, mode = 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)
    champions_list = json_data['league_champions_list']
    for i, champion in enumerate(champions_list, start=0):
        json_data['league_champions_dict'][champion]['eng name'] = league_eng_name_list[i]
        print(json_data['league_champions_dict'][champion]['eng name'])
with open(json_path, mode = 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, indent=4, ensure_ascii=False)