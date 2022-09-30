print("------------------------------------------------------------------------------")
print("Let me help you plan your day trip! Let's start with your desired destination.")
print("------------------------------------------------------------------------------")

def plan_itinerary():

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

    # ---------------------------- Restaurants Loop ---------------------------- 
    print("------------------------------------------------")
    print("Let's see if we can find you a great restaurant!")
    print("------------------------------------------------")

    restaurants = ["Slocum Joe's", "Cambridge Campus Diner", "Power Noodles"]
    chosen_resaurant = random.choice(restaurants)
    input_restaurants = input(f"How does '{chosen_resaurant}' sound for your restaurant? ")

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

    # ---------------------------- Transportations Loop ---------------------------- 
    print("-------------------------------------------")
    print("Let's get you a ride to your entertainment!")
    print("-------------------------------------------")

    transportations = ["Fast Travel", "Vertibird", "Power Armor"]
    chosen_transportation = random.choice(transportations)
    input_transportations = input(f"How does '{chosen_transportation}' sound for your transportation? ")

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

    # ---------------------------- Entertainments Loop ---------------------------- 
    print("----------------------------------------------------")
    print("Let's find you the BEST entertainment for your trip!")
    print("----------------------------------------------------")
        
    entertainments = ["Starlight Drive-In", "Dugout Inn", "Museum of Witchcraft"]
    chosen_entertainment = random.choice(entertainments)
    input_entertainments = input(f"How does '{chosen_entertainment}' sound for your entertainment? ")

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

    print(f"Looks like you're all set! Here is your completed itinerary. It includes...")

    for key, value in final_trip.items():
        print("")
        print(f"The desired {key} chosen was {value}")
        print("")

    input_choices_confirmation = input(f"Are you satisfied with your completed itinerary? ")

    valid_respons = False
    while valid_respons == False:

        if input_choices_confirmation == "yes":
            print("Great, it was my pleasure helping you plan your trip! Have fun.")
            valid_respons = True
            exit()
        elif input_choices_confirmation == "no":
            print("That's ok, which part of your trip would you like to edit? Please enter D for Destination, R for Restaurant, T for Transportation, E for Entertainment or N for None of it. ")
            if input_choices_confirmation == "D":
                chosen_destination = random.choice(destinations)
                input_destinations = input(f"How does '{chosen_destination}' sound for your destination? ")
                if input_destinations == "yes":
                    print("Ok, great!")
                    input_choices_confirmation = input(f"Are you satisfied with your completed itinerary? ")
                elif input_destinations == "no":
                    chosen_destination = random.choice(destinations)
                    input_destinations = input(f"How does '{chosen_destination}' sound for your destination? ")
                else:
                    print("I'm so sorry, I didnt catch that. Please enter yes or no ")
                    input_destinations = input(f"How does '{chosen_destination}' sound for your destination? ")
            elif input_choices_confirmation == "R":
                chosen_resaurant = random.choice(restaurants)
                input_restaurants = input(f"How does '{chosen_resaurant}' sound for your restaurant? ")
            elif input_choices_confirmation == "T":
                chosen_transportation = random.choice(transportations)
                input_transportations = input(f"How does '{chosen_transportation}' sound for your restaurant? ")
            elif input_choices_confirmation == "E":
                chosen_entertainment = random.choice(entertainments)
                input_entertainments = input(f"How does '{chosen_entertainment}' sound for your restaurant? ")
            elif input_choices_confirmation == "N":
                plan_itinerary()      
        else:
            print("I'm so sorry, I didnt catch that. Please enter yes or no ")
            input_choices_confirmation = input(f"Are you satisfied with your itinerary? ")

plan_itinerary()
