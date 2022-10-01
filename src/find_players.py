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
