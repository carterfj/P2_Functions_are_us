# Team 9
# IS 303 - Section 003
# Women's Soccer Season
# Description: This program will simulate a season for a women's soccer team. It will store information in a dictionary by asking about a home women’s soccer team, how many games they will play, and the name of the teams they will play. It will randomly generate scores for each game and determine if the home team won or lost. The program will then display the scores for each game, the final season record, and a message based on the record.

# import random module
import random

# list of all teams
teams = ['Alabama', 'Arizona', 'Arizona State', 'Arkansas', 'Auburn', 'Baylor', 'Boston College', 'BYU', 'California', 'Clemson', 'Colorado', 'Connecticut', 'Duke', 'Florida', 'Florida State', 'Georgia', 'Georgia Tech', 'Illinois', 'Indiana', 'Iowa', 'Iowa State', 'Kansas', 'Kansas State', 'Kentucky', 'Louisville', 'LSU', 'Maryland', 'Miami', 'Michigan', 'Michigan State', 'Minnesota', 'Mississippi State', 'Missouri', 'Nebraska', 'North Carolina', 'North Carolina State', 'Northwestern', 'Notre Dame', 'Ohio State', 'Oklahoma', 'Oklahoma State', 'Oregon', 'Oregon State', 'Penn State', 'Pittsburgh', 'Purdue', 'Rutgers', 'South Carolina', 'Stanford', 'Syracuse', 'Tennessee', 'Texas', 'Texas A&M', 'Texas Tech', 'UCLA', 'USC', 'Utah', 'Vanderbilt', 'Virginia', 'Virginia Tech', 'Wake Forest', 'Washington', 'Washington State', 'West Virginia', 'Wisconsin', 'Wyoming']

# store data in dictionary
seasonData = {
    'homeTeam': '',
    'numGames': 0,
    'games': [],
    'totalWins': 0,
    'totalLosses': 0
}

# main function to call other functions
def main():
    intro()

    # This outputs the correct information according to the users input from the menu
    while True:
        inputChoice = menu()
        if inputChoice == '1':
            break
        elif inputChoice == '2':
            print("You will select a team, play against random opponents, and track your wins and losses.")
            continue
        elif inputChoice == '3':
            displayRecord()
        else:
            print('Thanks for playing!')
            exit()

    teams[:] = random.sample(teams, seasonData['numGames'])
    for i in range(seasonData['numGames']):
        playGame(selectTeam('Choose a team to play against: '))
    displayRecord()

# intro function to display welcome message and prompt for user input
def intro():
    getHomeTeam()
    getNumGames()
    # 1. Keep the above two lines. Display an introduction to the game explaining rules and prompt for their name and display that in the welcome message. Return the name to the main program and store it in variable so it can be used throughout the program.
    print ("Welcome to the College Soccer Lookup!")
    print("You will select a team, play against random opponents, and track your wins and losses.")
    print ( "Let's get started.")

    user_name = input("what is your name?")
    print (f" Awesome {user_name} lets pick what you want to do!")

    return user_name




# Describe function here
def menu():
    print('Menu: ')
    print('1. Play Game')
    print('2. Read instructions')
    print('3. View final record')
    print('4. Exit Game')
    # This is the input from the user to choose an option
    userChoice = input('Enter a choice (1-4): ')
    return userChoice
# 2. Display of menu and return choice. Store in variable and use this value to determine which function to call next.

# Prompt user to select a team from the list of teams and remove the team from the list
def selectTeam(message = 'Select a team from the list above: '):
    print(teams)
    selection = input(message)
    if (selection in teams):
        teams.remove(selection)
        return selection
    else: 
        print('\nInvalid option. Please select a team from the list below\n')
        return selectTeam()


# prompt user for a home team and store in dictionary
def getHomeTeam():
    seasonData['homeTeam'] = selectTeam('Enter the name of your team (the home team): ')

# prompt user for the number of games in the season and store in dictionary
def getNumGames():
    numGames = int(input(f'Enter the number of teams that {seasonData['homeTeam']} will play (1-10): '))
    if numGames < 1 or numGames > 10:
        print('\nInvalid option. Please enter a number between 1 and 10\n')
        getNumGames()
    else:
        seasonData['numGames'] = numGames

# Describe function here.
# 4.Play the game receiving both team names. Generate random scores without ties. Return W or L. 
def playGame(homeTeam, awayTeam):
    homeScore = random.randint(0,50)
    awayScore = random.randint(0,50)
    while homeScore == awayScore:
        awayScore = random.randint(0,50)
        
    print(f'\n{homeTeam} : {homeScore} vs {awayTeam} : {awayScore}')

    if homeScore > awayScore:
        print(f'{homeTeam} wins!')
        return 'W'
    else:
        print(f'{awayTeam} wins!')
        return 'L'
    
    
# Describe function here.
def displayRecord():
    print('Display record.')
    # 5. Remove the above line. Display the final record for a team. Receive the home team data and display information.

# call main function to simulate a season
main()