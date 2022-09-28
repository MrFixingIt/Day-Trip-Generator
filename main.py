
print("------------------------------------------------------------------------------")
print("Let me help you plan your day trip! Let's start with your desired destination.")
print("------------------------------------------------------------------------------")
import random

# ---------------------------- Destinations Loop ---------------------------- 
destinations = ["Goodneighbor", "Diamond City", "Sanctuary Hills"]
chosen_destination = random.choice(destinations)
input_destinations = input(f"How does '{chosen_destination}' sound for your destination? ")

valid_respons = False
while valid_respons == False:

    if input_destinations == "yes":
        print(f"Excellent choice, I hear {chosen_destination} beautiful this time of year!")
        valid_respons = True
    elif input_destinations == "no":
        chosen_destination = random.choice(destinations)
        input_destinations = input(f"How does '{chosen_destination}' sound for your destination? ")
    else:
        print("I'm so sorry, I didnt catch that. Please enter yes or no ")
        input_destinations = input(f"How does '{chosen_destination}' sound for your destination? ")

print(f'Awesome, you have finalized {chosen_destination} as your desired destination!')

print("------------------------------------------------")
print("Let's see if we can find you a great restaurant!")
print("------------------------------------------------")

# ---------------------------- Restaurants Loop ---------------------------- 
restaurants = ["Slocum Joe's", "Cambridge Campus Diner", "Power Noodles"]
chosen_resaurant = random.choice(destinations)
input_restaurants = input(f"How does '{random.choice(restaurants)}' sound for your restaurant? ")

valid_respons = False
while valid_respons == False:

    if input_restaurants == "yes":
        print(f"I LOVE eating at {chosen_resaurant}! Their whole menu is amazing!")
        valid_respons = True
    elif input_restaurants == "no":
        chosen_resaurant = random.choice(restaurants)
        input_restaurants = input(f"How does '{chosen_resaurant}' sound for your destination? ")
    else:
        print("I'm so sorry, I didnt catch that. Please enter yes or no ")
        input_restaurants = input(f"How does '{chosen_resaurant}' sound for your destination? ")

print(f'Awesome, you have finalized {chosen_resaurant} as your desired restaurant!')

print("-------------------------------------------")
print("Let's get you a ride to your entertainment!")
print("-------------------------------------------")

# ---------------------------- Transportations Loop ---------------------------- 
transportations = ["Fast Travel", "Vertibird", "Power Armor"]
chosen_transportation = random.choice(transportations)
input_transportations = input(f"How does '{random.choice(transportations)}' sound for your transportation? ")

valid_respons = False
while valid_respons == False:

    if input_transportations == "yes":
        print(f"I've heard that traveling by {chosen_transportation} is very fun! I know you will enjoy it!")
        valid_respons = True
    elif input_transportations == "no":
        chosen_transportation = random.choice(transportations)
        input_transportations = input(f"How does '{chosen_transportation}' sound for your destination? ")
    else:
        print("I'm so sorry, I didnt catch that. Please enter yes or no ")
        input_transportations = input(f"How does '{chosen_transportation}' sound for your destination? ")

print(f'Awesome, you have finalized {chosen_transportation} as your desired transportation!')

print("----------------------------------------------------")
print("Let's find you the BEST entertainment for your trip!")
print("----------------------------------------------------")
    
# ---------------------------- Entertainments Loop ---------------------------- 
entertainments = ["Starlight Drive-In", "Dugout Inn", "Museum of Witchcraft"]
chosen_entertainment = random.choice(entertainments)
input_entertainments = input(f"How does '{random.choice(entertainments)}' sound for your entertainment? ")

valid_respons = False
while valid_respons == False:

    if input_entertainments == "yes":
        print(f"My friends and I went to the {chosen_entertainment} last year and we had a blast!")
        valid_respons = True
    elif input_entertainments == "no":
        chosen_entertainment = random.choice(entertainments)
        input_entertainments = input(f"How does '{chosen_entertainment}' sound for your destination? ")
    else:
        print("I'm so sorry, I didnt catch that. Please enter yes or no ")
        input_entertainments = input(f"How does '{chosen_entertainment}' sound for your destination? ")

print(f'Awesome, you have finalized {chosen_entertainment} as your desired entertainment!')

# ---------------------------- User Choices Confirmation ---------------------------- 
final_trip = {"destination": [chosen_destination], "restaurant": [chosen_resaurant], "transprtation": [chosen_transportation], "entertainment": [chosen_entertainment]}
user_choices = final_trip.items()
# print(f"Looks like you're all set! Here is your completed itinerary. It includes {chosen_destination} as your destination, {chosen_resaurant} as your restaurant, {chosen_transportation} as your transportation and {chosen_entertainment} as your entertainment.")
print(f"Looks like you're all set! Here is your completed itinerary. It includes {user_choices}.")

input_choices_confirmation = input(f"Are you satisfied with your itinerary? ")

valid_respons = False
while valid_respons == False:

    if input_choices_confirmation == "yes":
        print("Great, it was my pleasure helping you plan your trip. Have fun!")
        valid_respons = True
    elif input_choices_confirmation == "no":
        print("That's ok, let's start over from the beginning!")
        input_destinations = input(f"How does '{chosen_destination}' sound for your destination? ")
    else:
        print("I'm so sorry, I didnt catch that. Please enter yes or no ")
        input_choices_confirmation = input(f"Are you satisfied with your itinerary? ")

