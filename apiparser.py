import requests
import requests_cache
import datetime as t
from copy import deepcopy
from collections import OrderedDict
from operator import itemgetter

requests_cache.install_cache('riot_api_cache', backend='sqlite')

class API_PARSE():
    def __init__(self, api_key, name, champion=None):
        self.api_key = api_key
        self.name = name
        self.champion = champion
        self.payload = {'api_key': api_key}
        self.load_info()


    def load_info(self):
        self.summoner_info = self.get_summoner_info()
        self.winrate = self.get_weekly_stats()
        self.match_list, self.total_games, self.last_game_id = self.get_recent_matchlist(self.summoner_info['accountId'])
        self.game_timeline_chunk_list = self.get_match_timeline(self.last_game_id)
        self.participant_info, self.game_part_stats = self.get_match_info(self.last_game_id)
        self.junglers = self.get_junglers(self.game_part_stats)
        self.get_jungle_champ()


    def get_summoner_info(self):
        summoner_by_name_url = 'https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/%s' % self.name
        data = requests.get(summoner_by_name_url, params=self.payload)
        summoner_info = {key: data.json()[str(key)] for key in data.json()}
        now = t.datetime.now()
        print("Time: {0} / Used Cache: {1}".format(now, data.from_cache))
        return summoner_info


    def get_recent_matchlist(self, accountId):
        matchlist_by_accountId_url = 'https://euw1.api.riotgames.com/lol/match/v3/matchlists/by-account/%d/recent' % \
                                     accountId
        data = requests.get(matchlist_by_accountId_url, params=self.payload)
        matchlist = data.json()['matches']
        total_games = data.json()['totalGames']
        last_game_id = matchlist[0]['gameId']
        return matchlist, total_games, last_game_id


    def get_match_timeline(self, game_id):
        match_timeline_url = 'https://euw1.api.riotgames.com/lol/match/v3/timelines/by-match/%d' % game_id
        data = requests.get(match_timeline_url, params=self.payload)
        game_timeline_dic = {key: data.json()[str(key)] for key in data.json()}
        game_timeline_chunklist = game_timeline_dic['frames']
        return game_timeline_chunklist


    def get_match_info(self, game_id):
        match_info_url = 'https://euw1.api.riotgames.com/lol/match/v3/matches/%d' % game_id
        data = requests.get(match_info_url, params=self.payload)
        self.game_creation_timestamp = data.json()['gameCreation']
        game_participant_Id_list = data.json()['participantIdentities']
        participant_info = {player['participantId']: {'summonerId': player['player']['summonerId'],
                                                      'summonerName': player['player']['summonerName'],
                                                      'accountId': player['player']['accountId']}
                            for player in game_participant_Id_list}
        game_part_stats = data.json()['participants']
        return participant_info, game_part_stats


    def get_junglers(self, participant_stats):
        junglers = []
        for player in participant_stats:
            if player['timeline']['lane'] == 'JUNGLE':
                junglers.append({'participantId': player['participantId'],'championId': player['championId']})
        return junglers


    def get_jungle_champ(self):
        for jungler in self.junglers:
            champions_id_url = 'https://euw1.api.riotgames.com/lol/static-data/v3/champions/%d' \
                               % jungler['championId']
            data = requests.get(champions_id_url, params=self.payload)
            jungler.update({'name': data.json()['name']})


    def get_weekly_matchlist(self):
        time = int(t.datetime.timestamp(t.datetime.now()) * 1000)
        week_ago = int(t.datetime.timestamp(t.datetime.now() - t.timedelta(days=7)) * 1000)
        if self.champion is None:
            payload = {'endTime': time, 'beginTime': week_ago, 'api_key': api_key}
        else:
            champions_url = 'https://euw1.api.riotgames.com/lol/static-data/v3/champions'
            data = requests.get(champions_url, params=self.payload)
            champion_id = data.json()['data'][self.champion]['id']
            payload = {'endTime': time, 'beginTime': week_ago, 'champion': champion_id, 'api_key': api_key}
        weekly_matchlist_url = 'https://euw1.api.riotgames.com/lol/match/v3/matchlists/by-account/%d' % \
                               self.summoner_info['accountId']
        data = requests.get(weekly_matchlist_url, params=payload)
        matchlist = data.json()['matches']
        total_games = data.json()['totalGames']
        last_game_id = matchlist[0]['gameId']
        return matchlist, total_games, last_game_id


    def get_weekly_stats(self):
        matchlist, total_games, last_game_id = self.get_weekly_matchlist()
        win = 0
        champ_win, o_items = {}, {'item%d' % n: [] for n in range(7)}
        part_id = None
        for match in matchlist:
            participant_info, game_part_stats = self.get_match_info(match['gameId'])
            items = deepcopy(o_items)
            champ_id = match['champion']
            champions_id_url = 'https://euw1.api.riotgames.com/lol/static-data/v3/champions/%d' % champ_id
            data = requests.get(champions_id_url, params=self.payload)
            champion_name = data.json()['name']
            if champion_name in champ_win:
                champ_win[champion_name]['total_games'] += 1
            else:
                champ_win.update({champion_name: {'win': 0, 'total_games': 1, 'items': items}})
            for Id, info in participant_info.items():
                if info['summonerName'] == self.name:
                    part_id = Id
            for participant in game_part_stats:
                if participant['participantId'] == part_id:
                    for n in range(7):
                        for item_str, x in champ_win[champion_name]['items']['item%d' % n]:
                            if str(participant['stats']['item%d' % n]) not in champ_win[champion_name]['items']['item%d' % n]:
                                champ_win[champion_name]['items']['item%d' % n].append((str(participant['stats']['item%d' % n]), 1))
                            else:
                                champ_win[champion_name]['items']['item%d' % n][1] += 1
                    if participant['stats']['win'] == True:
                        win += 1
                        champ_win[champion_name]['win'] += 1
        for champ in champ_win:
            for item in champ_win[champ]['items']:
                champ_win[champ]['items'][item]
        winrate = win/total_games
        item_stats = self.evaluate_items(champ_win)
        if self.champion != None:
            return self.champion+': '+'{0:.0f}%'.format(winrate * 100)
        else:
            return champ_win


    def evaluate_items(self, dic):
        item_stat_dic = OrderedDict()
        list = []
        for champ in dic:
            list.append((champ, dic[champ]['total_games']))
        list = sorted(list, key=itemgetter(1), reverse=True)
        #for champ, total_games in list:
            #item_stat_dic.update({champ: {'item0': }})


api_key = ''
name = 'BreakfastinMODA'
H = API_PARSE(api_key, name,'Lulu')
print(H.winrate)