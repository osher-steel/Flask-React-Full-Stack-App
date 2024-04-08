from results import get_results
from odds import get_odds
import datetime

# 4 options: over, under, home win , away win
# To place a bet we need to store: the game key, the bet type, the price and the line if needed
def place_bet(game_key, bet_type, price, line):
    # Ex
    game_key = '2024-04-03CHAPOR'
    bet_type = 'over'
    price = '1.91'
    line = '213.0'
    status = "Waiting"

    # Store that in the db
    # cur.execute("INSERT INTO Bet(GameID,BetType,Price,Line,Status)VALUES(?,?,?,?,?);", 
    # (game_key,bet_type,price,line,status)


def check_bet(game_key,account_id):
    # Look up row in Bet table that matches gameID and accountID
    # Get date and convert to 'YYYY-MM-DD' format
    # Get home team, visitor team, bet type, line, price
    visitor_team = 'Toronto Raptors'
    home_team = 'Minnesota Timberwolves'  
    bet_type = 'Over' 
    price = '1.91'
    line = '210'
    date = '2024-04-04'
    games = get_results(date)

    for game in games:
        if game['home_team'] == home_team and game['visitor_team'] == visitor_team:
            # Game is not finished
            if game['visitor_points'] is None:
                return 0
            else:
                status = bet_status(game['bet_type'], game['home_points'],game['visitor_points'],game['line'])
                # Modify row with new status
                if status =="Win":
                    money = 0
                    # Insert money * price_multiplier to user's account

                return 1
    
    # Did not find game
    return 0

def bet_status(bet_type,home_points,visitor_points,line):
    home_points = int(home_points)
    visitor_points = int(visitor_points)
    if (bet_type == "Over" and home_points + visitor_points > line)                                    or (bet_type == "Under" and home_points + visitor_points < line)                                   or (bet_type == "Home Win" and home_points > visitor_points)                                         or(bet_type == "Away Win" and home_points < visitor_points): 
        return "Win"
    else:
        return "Lose"



if __name__ == "__main__":
    place_bet()