from pprint import pprint
import src.find_players as fp

def intro_txt():
  print("Welcome to Who Made That Dunk?")
  print("\n")

def basic_return():
  fname = input("Enter the first name you're searching for.")
  lname = input("Enter the last name you're searching for.")
  
  values = fp.return_players(fname, lname)
  
  pprint(values, width=2)
