import requests
import json
import time

# url = "https://api-football-v1.p.rapidapi.com/v2/predictions/240997"
headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "43de0b8110msha8c6361fdddf427p1194c1jsn756bf8944a3a"
}

# response = requests.request("GET", url, headers=headers)

output = open("predictions.txt","w")
f = open("matches.txt")
lines = f.readlines()
for line in lines:
    fixture = line.split('--')[0]
    print(fixture)
    url = "https://api-football-v1.p.rapidapi.com/v2/predictions/{fixture}".format(fixture = fixture)
    response = requests.request("GET", url, headers=headers)
    prediction_dic=json.loads(response.text)
    prediction = prediction_dic['api']['predictions'][0]
    
    home = prediction['teams']['home']['team_name']
    away = prediction['teams']['away']['team_name']
    advice = prediction['advice']
    home_percent = prediction['winning_percent']['home']
    draws_percent = prediction['winning_percent']['draws']
    away_percent = prediction['winning_percent']['away']

    info = """
        home:{home},
        away:{away},
        advice:{advice},
        home_win:{home_percent},
        draws:{draws_percent},
        away_win:{away_percent}
    """.format(home=home,away=away,advice=advice,home_percent=home_percent,draws_percent=draws_percent,away_percent=away_percent)
    output = open("predictions.txt","a")
    output.write(info)
    output.write('\n')
    output.write('------------------')
    output.write('\n')
    time.sleep(3)
    output.close()

    