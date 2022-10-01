from nba_api.stats.static import players
import json


def get_all_players():
  with open('data.json', 'w') as f:
    data = players.get_players()
    json.dump(data, f)


def load_all_players():
  with open('data.json', 'r') as f:
    data = json.load(f)
    return data


def return_players(fname=None, lname=None):
  f = load_all_players()
  found = []
  if fname and lname:
    for player in f:
      if player['first_name'] == fname and player['last_name'] == lname:
        found.append(player)
  elif fname and not lname:
    for player in f:
      if player['first_name'] == fname:
        found.append(player)
  elif lname and not fname:
    for player in f:
      if player['last_name'] == lname:
        found.append(player)
  else:
    found.append(f)
  return found
