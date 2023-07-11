import os
import random

STATE_TO_CAP_DICT = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'  
}

CAP_TO_STATE_DICT = dict(map(reversed, STATE_TO_CAP_DICT.items()))

def guessCapitals() :
    # Game state variables
    num_rounds = 0
    num_correct = 0

    # Create random ordered array for states
    states = list(STATE_TO_CAP_DICT.keys())
    random.shuffle(states)

    # Initial text
    os.system('clear')
    print("=== How to play ===")
    print("\nYou will be given the name of a state, and you need to enter its capital")
    print("\nEnter \"exit\" or \"quit\" to exit")
    print("Enter \"menu\" to go back to the main menu\n")

    input("Press Enter to begin")

    # Game loop
    os.system('clear')
    keep_playing = True
    while(keep_playing) :
        # Print state of the game
        print("Score: " + str(num_correct) + "/" + str(num_rounds))
        # Edge case, don't divide by 0!
        if (num_rounds == 0) :
            print("Accuracy: 0%")
        else :
            print("Accuracy: " + str(int(num_correct / float(num_rounds) * 100)) + "%")

        print("")
        
        # Update the round number
        num_rounds += 1

        # Get the state to guess
        state_index = random.randint(0, 24) # Only get from the first half of the list, so we can be sure things get randomized
        state = states.pop(state_index) # Remove from list
        states.append(state) # Add it to end of the list so it doesn't come back soon

        # Get its capital
        correct_capital = STATE_TO_CAP_DICT.get(state, "")

        print("What is the capital of " + state + "?")
        capital_guess = input(">> ")

        # Clear the terminal each round (I want the feedback visible though)
        os.system('clear')

        # Check for quitting / menu
        if (capital_guess.lower() in ["quit", "exit"]) :
            keep_playing = False
        elif (capital_guess.lower() == "menu") :
            keep_playing = False
            mainMenu()
        else :
            if (capital_guess.lower() == correct_capital.lower()) :
                print("Correct! The capital of " + state + " is " + correct_capital + "!")
                num_correct += 1
            else :
                print("Incorrect. The capital of " + state + " is " + correct_capital + "!")
        
        print("")
    

def guessStates() :
    # Game state variables
    num_rounds = 0
    num_correct = 0

    # Create random ordered array for states
    capitals = list(CAP_TO_STATE_DICT.keys())
    random.shuffle(capitals)

    # Initial text
    os.system('clear')
    print("=== How to play ===")
    print("\nYou will be given a capital city, and you need to enter what state it's the capital for")
    print("\nEnter \"exit\" or \"quit\" to exit")
    print("Enter \"menu\" to go back to the main menu\n")

    input("Press Enter to begin")

    # Game loop
    os.system('clear')
    keep_playing = True
    while(keep_playing) :
        # Print state of the game
        print("Score: " + str(num_correct) + "/" + str(num_rounds))
        # Edge case, don't divide by 0!
        if (num_rounds == 0) :
            print("Accuracy: 0%")
        else :
            print("Accuracy: " + str(int(num_correct / float(num_rounds) * 100)) + "%")

        print("")
        
        # Update the round number
        num_rounds += 1

        # Get the capital to guess
        capital_index = random.randint(0, 24) # Only get from the first half of the list, so we can be sure things get randomized
        capital = capitals.pop(capital_index) # Remove from list
        capitals.append(capital) # Add it to end of the list so it doesn't come back soon

        # Get its state
        correct_state = CAP_TO_STATE_DICT.get(capital, "")

        print(capital + " is the capital of what state?")
        state_guess = input(">> ")

        # Clear the terminal each round (I want the feedback visible though)
        os.system('clear')

        # Check for quitting / menu
        if (state_guess.lower() in ["quit", "exit"]) :
            keep_playing = False
        elif (state_guess.lower() == "menu") :
            keep_playing = False
            mainMenu()
        else :
            if (state_guess.lower() == correct_state.lower()) :
                print("Correct! The capital of " + state_guess + " is " + correct_state + "!")
                num_correct += 1
            else :
                print("Incorrect. The capital of " + state_guess + " is " + correct_state + "!")

        print("")

def mainMenu() :
    # Setup
    os.system('clear')
    print("==================================")
    print("**********************************")
    print("Welcome to Unnamed Geography Game!")
    print("**********************************")
    print("==================================")
    print("\nEnter the corresponding number to select your game mode\n")
    print("1) Given states guess capitals")
    print("2) Given capitals guess states")
    print("3) Exit\n")

    # Get initial response
    has_valid_response = False
    while (not has_valid_response) :
        game_choice = input("Your choice >> ")
        
        # Check if not int so cast doesn't fail
        if (not game_choice.isdigit()) :
            print("That's literally not even a number, try again")
        else :
            # Cast for future checks
            game_choice = int(game_choice)

            if (game_choice == 69) :
                print(":)")
            elif (game_choice == 420) :
                print(">:(")
            elif (game_choice in [1,2,3]) :
                has_valid_response = True
            else :
                print("Not an option smh, try again")

    game_choice = int(game_choice)

    if (game_choice == 1) :
        guessCapitals()
    elif (game_choice == 2) :
        guessStates()

mainMenu()