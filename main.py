import json
import requests
import psycopg2
import time


def getApiKey():
    with open('api_key.txt') as file:
        api_key = file.read()
    return api_key


def getResponse(region, api):
    api_key = getApiKey()
    url = "https://" + region + ".api.riotgames.com" + api + "?api_key=" + api_key
    response = requests.get(url)
    return response


def getSummonerData(summoner_name, routing_value):
    response = getResponse(routing_value, "/lol/summoner/v4/summoners/by-name/" + summoner_name)
    count = 1
    while response.status_code >= 400:
        print("No response")
        time.sleep(1)
        print("Sleep ", count)
        count += 1
        response = getResponse(routing_value, "/lol/summoner/v4/summoners/by-name/" + summoner_name)
    return json.loads(response.text)


def getSummonerPuuID(summoner_name, routing_value):
    return getSummonerData(summoner_name, routing_value)['puuid']


def getLastMatchesIds(region, puuid):
    response = getResponse(region, "/lol/match/v5/matches/by-puuid/" + puuid + "/ids")
    return json.loads(response.text)
    # Last 20 matches
    # EUROPE


def getMatchData(region, match_id):
    response = getResponse(region, "/lol/match/v5/matches/" + match_id)
    return json.loads(response.text)


def getLeague(region):
    response = getResponse(region, "/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5")
    return json.loads(response.text)


conn = psycopg2.connect(host="localhost", database="lol_insights", user="lol_insights_admin", password="mmurwmzi20")
server_routing_values = conn.cursor()
server_routing_values.execute("SELECT DISTINCT server_routing_value FROM lol_insights.lol_data.servers_info;")

server_routing_values_list = []
for val in server_routing_values:
    server_routing_values_list.append(val[0])


entries_list = []

for routing_value in server_routing_values_list:
    print((getLeague(routing_value)['entries'])[0])
    #for e in entries:
        #summoner_puuid = getSummonerPuuID(e['summonerName'], routing_value)
        #entries_list.append([e['summonerId'] + e['summonerName'] + str(e['wins']) + str(e['losses']) + str(summoner_puuid) + routing_value])

print(len(entries_list))
for entry in entries_list:
    print(entry)

conn.commit()
server_routing_values.close()
conn.close()
# %%
