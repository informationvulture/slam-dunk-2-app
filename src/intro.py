from pprint import pprint
import src.find_players as fp


def intro_txt():
  print("*********************************************")
  print("\n")
  print("Welcome to Who Made That Dunk?")
  print("\n")
  print("The way this app works is using either the first or last name",
        end=" ")
  print("you can find your favourite player.")
  print("\n")
  print("TIP: You don't have to fill in all the blanks!")
  print("*********************************************")
  print("\n")


def basic_return():
  fname = input("Enter the first name you're searching for: ")
  lname = input("Enter the last name you're searching for: ")
  print("\n")

  values = fp.return_players(fname, lname)
  full_data = fp.print_players(values)

  for c,v in enumerate(full_data):
    print(f"{c+1}: {v}")
  if len(full_data) > 10:
    print("Wow, so many players with the same name!")
