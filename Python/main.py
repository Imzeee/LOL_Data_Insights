import json
import requests


def getApiKey():
    with open('api_key.txt') as file:
        api_key = file.read()
    return api_key


def getResponse(region, api):
    api_key = getApiKey()
    url ="https://" + region + ".api.riotgames.com" + api + "?api_key=" + api_key
    return requests.get(url)


def getSummonerData(summoner_name):
    response = getResponse("eun1", "/lol/summoner/v4/summoners/by-name/"+summoner_name)
    return json.loads(response.text)


def getSummonerPuuID(summoner_name):
    return getSummonerData(summoner_name)['puuid']


def getLastMatchesIds(region, puuid):
    response = getResponse(region, "/lol/match/v5/matches/by-puuid/"+puuid+"/ids")
    return json.loads(response.text)
    # Last 20 matches
    # EUROPE


def getMatchData(region, match_id):
    response = getResponse(region, "/lol/match/v5/matches/"+match_id)
    return json.loads(response.text)


def getLeague(region):
    response = getResponse(region, "/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5")
    return json.loads(response.text)



