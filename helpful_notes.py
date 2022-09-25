
my_dictionary = {
    "Destinations": ["Goodneighbor", "Diamond City", "Sanctuary Hills"],
    "Restaurants": ["Slocum Joe's", "Cambridge Campus Diner", "Power Noodles"],
    "Transportations": ["Fast Travel", "Vertibird", "Power Armor"],
    "Entertainments": ["Starlight Drive-In", "Dugout Inn", "Museum of Witchcraft"]
}


import random
user_input = input("Where would you like to go on your trip? ")
user_choice = input(" Type Goodneighbor, Diamond City, Sanctuary Hills: ")

valid_respons = True
while valid_respons == True:
    if user_choice in "Destinations":
        print("Excellent choice, I hear it's beautiful this time of year!")
else:
    print("I am so sorry, this destination is currently unavailable.")


# ---------- Rock, Paper, Scissor Game ---------- 
import random
CHOICES = ["rock", "paper", "scissors"]
print("Make your throw")
user_choice = input(" Type rock, paper, scissors: ")
if user_choice in CHOICES:
    computer_choice = random.choice(CHOICES)
    print(
        f"\nYou threw '{user_choice}', the computer threw '{computer_choice}'"
    )
else:
    print(f"\nYou typed '{user_choice}' which isn't a valid throw")


# ---------- Task #4 Print 3 or Bigger String ---------- 
user_input = input("Choose a word. ")
valid_respons = True
while valid_respons == True:

    if len(user_input) >= 3:
        print(user_input)
        valid_respons = False
    else:
        print("We need a larger string to print!")
        user_input = input("Choose a word. ")


def pick_from_list(lst: list) -> object:
    return random.choice(lst)
