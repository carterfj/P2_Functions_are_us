# Team 9
# IS 303 - Section 003
# Women's Soccer Season
# Description: This program will simulate a season for a women's soccer team. It will store information in a dictionary by asking about a home women’s soccer team, how many games they will play, and the name of the teams they will play. It will randomly generate scores for each game and determine if the home team won or lost. The program will then display the scores for each game, the final season record, and a message based on the record.

# import random module
import random

# store season data in dictionary
seasonData = {}

# main function to call other functions
def main():
    # initialize game
    reset()
    intro()
    teams[:] = random.sample(teams, seasonData['numGames'])
    inputChoice = '0'

    # loop through menu options until user exits
    while (inputChoice != '4'):
        inputChoice = menu()
        if inputChoice == '1':
            if (len(teams) > 0):
                playGame(seasonData['homeTeam'], selectTeam('Choose a team to play against: '))
            else:
                reset()
                intro()
                teams[:] = random.sample(teams, seasonData['numGames'])
        elif inputChoice == '2':
            print("You will select a team, play against random opponents, and track your wins and losses.")
        elif inputChoice == '3':
            displayRecord()
        else:
            print('Thanks for playing!')

# function to reset the game
def reset():
    # set season data to default values
    seasonData.update({
    'userName': '',
    'homeTeam': '',
    'numGames': 0,
    'totalWins': 0,
    'totalLosses': 0
    })
    # list of all teams
    global teams
    teams = ['Alabama', 'Arizona', 'Arizona State', 'Arkansas', 'Auburn', 'Baylor', 'Boston College', 'BYU', 'California', 'Clemson', 'Colorado', 'Connecticut', 'Duke', 'Florida', 'Florida State', 'Georgia', 'Georgia Tech', 'Illinois', 'Indiana', 'Iowa', 'Iowa State', 'Kansas', 'Kansas State', 'Kentucky', 'Louisville', 'LSU', 'Maryland', 'Miami', 'Michigan', 'Michigan State', 'Minnesota', 'Mississippi State', 'Missouri', 'Nebraska', 'North Carolina', 'North Carolina State', 'Northwestern', 'Notre Dame', 'Ohio State', 'Oklahoma', 'Oklahoma State', 'Oregon', 'Oregon State', 'Penn State', 'Pittsburgh', 'Purdue', 'Rutgers', 'South Carolina', 'Stanford', 'Syracuse', 'Tennessee', 'Texas', 'Texas A&M', 'Texas Tech', 'UCLA', 'USC', 'Utah', 'Vanderbilt', 'Virginia', 'Virginia Tech', 'Wake Forest', 'Washington', 'Washington State', 'West Virginia', 'Wisconsin', 'Wyoming']

# 1. Display an introduction to the game explaining rules and prompt for their name and display that in the welcome message. Return the name to the main program and store it in variable so it can be used throughout the program.
def intro():
    print ("Welcome to the College Soccer Lookup!")
    print("You will select a team, play against random opponents, and track your wins and losses.")
    print ( "Let's get started.")

    seasonData['userName'] = input("what is your name? ")
    print (f"Awesome {seasonData['userName']} lets pick what you want to do!")
    getHomeTeam()
    getNumGames()

# 2. Display of menu and return choice. Store in variable and use this value to determine which function to call next.
def menu():
    if (len(teams) > 0):
        print('Menu:\n1. Play Game')
    else:
        displayRecord()
        print('Menu:\n1. Start a new season')
    print('2. Read instructions')
    print('3. View record')
    print('4. Exit Game')
    # This is the input from the user to choose an option
    userChoice = input('Enter a choice (1-4): ')
    return userChoice

# 3. Prompt user to select a team from the list of teams and remove the team from the list
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

# 4. Play the game receiving both team names. Generate random scores without ties. Return W or L. 
def playGame(homeTeam, awayTeam):
    homeScore = random.randint(0,10)
    awayScore = random.randint(0,10)
    while homeScore == awayScore:
        awayScore = random.randint(0,10)
        
    print(f'\n{homeTeam} : {homeScore} vs {awayTeam} : {awayScore}')

    if homeScore > awayScore:
        seasonData['totalWins'] += 1
        print(f'{homeTeam} wins!')
        return 'W'
    else:
        seasonData['totalLosses'] += 1
        print(f'{awayTeam} wins!')
        return 'L'
    
# 5. Display the final record for a team. Receive the home team data and display information.
def displayRecord():
    home_team = seasonData['homeTeam']
    iWins = seasonData['totalWins']
    iLosses = seasonData['totalLosses']
    
    print(f"\nSeason Record for {home_team}: ")
    print(f"Wins: {iWins} | Losses: {iLosses}")
    
    if len(teams) == 0:
        # Calculate for win rate
        iTotalGameCnt = iWins + iLosses
        fWinRate = iWins / iTotalGameCnt

        if fWinRate >= 0.75:
            print("Qualified for the NCAA Women's Soccer Tournament")
        elif fWinRate >= 0.5:
            print("You had a good season")
        else:
            print("Your team needs to practice!")

# call main function to simulate a season
main()
