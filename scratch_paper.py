print("---------------------")
print("Let's plan your trip!")
print("---------------------")

Destinations = ["Goodneighbor", "Diamond City", "Sanctuary Hills"]
Restaurants = ("Slocum Joe's", "Cambridge Campus Diner", "Power Noodles")
Transportations = ("Fast Travel", "Vertibird", "Power Armor")
Entertainments = ("Starlight Drive-In", "Dugout Inn", "Museum of Witchcraft")
import random
input_Destinations = input(f"How does '{random.choice(Destinations)}' sound for your destination? ")
ok_input_Destinations = input(f"Okay, how does '{random.choice(Destinations)}' sound for your destination? ")
input_Restaurants = input(f"How does '{random.choice(Restaurants)}' sound for your restaurant? ")
ok_input_Restaurants = input(f"Okay, how does '{random.choice(Restaurants)}' sound for your restaurant? ")
input_Transportations = input(f"How does '{random.choice(Transportations)}' sound for your transportation? ")
ok_input_Transportations = input(f"Okay, how does '{random.choice(Transportations)}' sound for your transportation? ")
input_Entertainments = input(f"How does '{random.choice(Entertainments)}' sound for your entertainment? ")
ok_input_Entertainments = input(f"Okay, how does '{random.choice(Entertainments)}' sound for your entertainment? ")

# ------------------ Destinations ------------------ 
print(input_Destinations)
while input_Destinations == " yes":
    print("Excellent choice, I hear it's beautiful this time of year!")
    continue
while input_Destinations == " no":
    print(ok_input_Destinations)
else:
    print("I'm so sorry, that destination is temporarily restricted due to Covid...")
    input(input_Destinations)

# ------------------- Restaurants ------------------- 
print(input_Restaurants)
while input_Restaurants == " yes":
    print("I LOVE eating there! Their whole menu is amazing!")
    continue
while input_Restaurants == " no":
    input(ok_input_Restaurants)
else:
    print("I'm so sorry, that restaurant is currently closed due to renovations...")
    input(input_Restaurants)

# ------------------- Transportations ------------------ 
print(input_Transportations)
while input_Transportations == " yes":
    print("I've heard that traveling like that is very fun! I know you will enjoy it!")
    continue
while input_Transportations == " no":
    input(ok_input_Transportations)
else:
    print("My appologese, that mode of transportation has been down for repairs...")
    input(input_Transportations)
    
# ------------------- Entertainments ------------------ 
print(input_Entertainments)
while input_Entertainments == " yes":
    print("My friends and I went there last year and we had a blast!")
    continue
while input_Entertainments == " no":
    input(ok_input_Entertainments)
else:
    print("Unfortunatly, that entertainment venue was sold out weeks ago...")
    input(input_Entertainments)