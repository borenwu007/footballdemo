import requests
import json

def get_match_file(url):
    
    querystring = {"timezone":"Europe/London"}

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "43de0b8110msha8c6361fdddf427p1194c1jsn756bf8944a3a"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    fixture_dic=json.loads(response.text)

    output_file = open('matches.txt','w')

    for fixture in fixture_dic['api']['fixtures']:
        output_file.write('{fixture_id}--{homeTeam} : {awayTeam}'.format(fixture_id=fixture['fixture_id'],homeTeam=fixture['homeTeam']['team_name'],awayTeam=fixture['awayTeam']['team_name']))
        output_file.write('\n')



if __name__ == '__main__':
    url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/league/514/2019-12-12"
    get_match_file(url)