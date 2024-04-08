import requests

# date has to be in the format 'YYYY-MM-DD'
def get_results(date):
    url = "https://api-nba-v1.p.rapidapi.com/games"

    querystring = {"date":date}

    headers = {
        "X-RapidAPI-Key": "b32a2e36fbmshd22362ae58d4d2fp142d89jsnfd4f85576b32",
        "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    nba_json = response.json()

    results = []

    for game in nba_json['response']:
        visitor_name = game['teams']['visitors']['name']
        visitor_points = game['scores']['visitors']['points']
        home_name = game['teams']['home']['name']
        home_points = game['scores']['home']['points']

        result = {'visitor_team':visitor_name,'visitor_points':visitor_points,
            'home_team':home_name,'home_points':home_points}
        
        results.append(result)

    return results

if __name__ == "__main__":
    results = get_results('2024-04-04')
    print(results)