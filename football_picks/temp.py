from sportsreference.nfl.boxscore import Boxscores

games_today = Boxscores(1, 2020)
# Prints a dictionary of all matchups for week 1 of 2017
games = games_today.games['1-2020']
ret = []
for g in games:
    outcomes = {}
    outcomes["away_name"] = g['away_name']
    outcomes["away_score"] = g['away_score']
    outcomes['home_name'] = g['home_name']
    outcomes['home_score'] = g['home_score']
    ret.append(outcomes)
print(ret)