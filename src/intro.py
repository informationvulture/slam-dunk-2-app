from pprint import pprint
import src.find_players as fp

def intro_txt():
  print("*********************************************")
  print("\n")
  print("Welcome to Who Made That Dunk?")
  print("\n")
  print("*********************************************")

def basic_return():
  fname = input("Enter the first name you're searching for.")
  lname = input("Enter the last name you're searching for.")
  
  values = fp.return_players(fname, lname)
  
  pprint(values, width=2)
  if len(values) > 10:
    print("Wow, so many players with the same name!")
