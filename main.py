import src.find_players as fp
from pprint import pprint

# If you need to call the API, run this:
# fp.get_all_players()

players = fp.load_all_players()
pprint([i for i in players if i['last_name'] == "Smith"], width=1)