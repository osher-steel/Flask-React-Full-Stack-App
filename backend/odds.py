import requests

API_KEY = '2e45b517a7f1b28c45fac18d4eefd331'

SPORT = 'basketball_nba'
REGIONS = 'us' 
MARKETS = 'totals,h2h' 
ODDS_FORMAT = 'decimal' 
DATE_FORMAT = 'iso'
BOOKMAKERS = 'fanduel'

def api_odds():

    odds_response = requests.get(
        f'https://api.the-odds-api.com/v4/sports/{SPORT}/odds',
        params={
            'api_key': API_KEY,
            'regions': REGIONS,
            'markets': MARKETS,
            'oddsFormat': ODDS_FORMAT,
            'dateFormat': DATE_FORMAT,
            'bookmakers': BOOKMAKERS
        }
    )

    if odds_response.status_code != 200:
        print(f'Failed to get odds: status_code {odds_response.status_code}, response body {odds_response.text}')
        return None
    else:
        odds_json = odds_response.json()

        games = []
        for game in odds_json:
            time = game["commence_time"]
            home_team = game["home_team"]
            visitor_team = game["away_team"]
            line = game["bookmakers"][0]["markets"][1]["outcomes"][0]["point"]
            over_price = game["bookmakers"][0]["markets"][1]["outcomes"][0]["price"]
            under_price = game["bookmakers"][0]["markets"][1]["outcomes"][1]["price"]

            head2head = []
            head2head.append({"team_name":game["bookmakers"][0]["markets"][0]["outcomes"][0]["name"],
                        "price": game["bookmakers"][0]["markets"][0]["outcomes"][0]["price"]})
            head2head.append({"team_name":game["bookmakers"][0]["markets"][0]["outcomes"][1]["name"],
                    "price": game["bookmakers"][0]["markets"][0]["outcomes"][1]["price"]})
            
            # Onlye need the date for the key
            key = time[0:10] + home_team + visitor_team

            g = {"key":key, "time":time,"home_team":home_team,"visitor_team":visitor_team,"line":line,"over_price":over_price,"under_price":under_price, "h2h":head2head}
            games.append(g)

        return games

        # Games
        # List of dicts for each game
        # Each game dict has time, home team, away team, line, over and under price and h2h dict
        # h2h dict has two dicts with each team_name and price

        # Check the usage quota
        # print('Remaining requests', odds_response.headers['x-requests-remaining'])
        # print('Used requests', odds_response.headers['x-requests-used'])

if __name__ == "__main__":
    print(api_odds())