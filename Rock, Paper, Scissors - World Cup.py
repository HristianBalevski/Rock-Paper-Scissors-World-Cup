import random
list_of_countries = ['argentina', 'brazil', 'china', 'denmark', 'egypt', 'france', 'germany', 'hungary', 'italy',
                     'jamaica', 'kuwait', 'latvia', 'mexico', 'netherlands', 'oman', 'portugal', 'qatar', 'russia',
                     'spain', 'turkey', 'ukraine', 'venezuela', 'yemen', 'zambia']

# These are all countries on the world cup.
argentina = 'Argentina'
brazil = 'Brazil'
china = 'China'
denmark = 'Denmark'
egypt = 'Egypt'
france = 'France'
germany = 'Germany'
hungary = 'Hungary'
italy = 'Italy'
jamaica = 'Jamaica'
kuwait = 'Kuwait'
latvia = 'Latvia'
mexico = 'Mexico'
netherlands = 'Netherlands'
oman = 'Oman'
portugal = 'Portugal'
qatar = 'Qatar'
russia = 'Russia'
spain = 'Spain'
turkey = 'Turkey'
ukraine = 'Ukraine'
venezuela = 'Venezuela'
yemen = 'Yemen'
zambia = 'Zambia'

# The player have to choose a number, and then he will see with which country he gonna plays on the final.
player_move = input("Choose a number between 1 and 24: ")
favorite_team = ''

if player_move == '1':
    favorite_team = argentina
elif player_move == '2':
    favorite_team = brazil
elif player_move == '3':
    favorite_team = china
elif player_move == '4':
    favorite_team = denmark
elif player_move == '5':
    favorite_team = egypt
elif player_move == '6':
    favorite_team = france
elif player_move == '7':
    favorite_team = germany
elif player_move == '8':
    favorite_team = hungary
elif player_move == '9':
    favorite_team = italy
elif player_move == '10':
    favorite_team = jamaica
elif player_move == '11':
    favorite_team = kuwait
elif player_move == '12':
    favorite_team = latvia
elif player_move == '13':
    favorite_team = mexico
elif player_move == '14':
    favorite_team = netherlands
elif player_move == '15':
    favorite_team = oman
elif player_move == '16':
    favorite_team = portugal
elif player_move == '17':
    favorite_team = qatar
elif player_move == '18':
    favorite_team = russia
elif player_move == '19':
    favorite_team = spain
elif player_move == '20':
    favorite_team = turkey
elif player_move == '21':
    favorite_team = ukraine
elif player_move == '22':
    favorite_team = venezuela
elif player_move == '23':
    favorite_team = yemen
elif player_move == '24':
    favorite_team = zambia
else:
    raise SystemExit("Invalid Input. Please try again.")
print(f'Your Favorite Team is {favorite_team}.')

# The computer generates a random number that shows the second country on the final.
computer_move = random.randint(1, 24)
computer_team = ''

if computer_move == 1:
    computer_team = argentina
elif computer_move == 2:
    computer_team = brazil
elif computer_move == 3:
    computer_team = china
elif computer_move == 4:
    computer_team = denmark
elif computer_move == 5:
    computer_team = egypt
elif computer_move == 6:
    computer_team = france
elif computer_move == 7:
    computer_team = germany
elif computer_move == 8:
    computer_team = hungary
elif computer_move == 9:
    computer_team = italy
elif computer_move == 10:
    computer_team = jamaica
elif computer_move == 11:
    computer_team = kuwait
elif computer_move == 12:
    computer_team = latvia
elif computer_move == 13:
    computer_team = mexico
elif computer_move == 14:
    computer_team = netherlands
elif computer_move == 15:
    computer_team = oman
elif computer_move == 16:
    computer_team = portugal
elif computer_move == 17:
    computer_team = qatar
elif computer_move == 18:
    computer_team = russia
elif computer_move == 19:
    computer_team = spain
elif computer_move == 20:
    computer_team = turkey
elif computer_move == 21:
    computer_team = ukraine
elif computer_move == 22:
    computer_team = venezuela
elif computer_move == 23:
    computer_team = yemen
elif computer_move == 24:
    computer_team = zambia
if computer_team == favorite_team:
    computer_team = list_of_countries[computer_move + 1]
    if list_of_countries[computer_move + 1] == 24:
        computer_team = list_of_countries[0]
print(f"The Favorite Team of Your Opponent is {computer_team}.")
print()
print(f"Let's start!")

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_points = 0
computer_points = 0
game_counter = 0

while game_counter != 10:
    player_action = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_action == "r":
        player_action = rock
    elif player_action == "p":
        player_action = paper
    elif player_action == "s":
        player_action = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")

    computer_action = random.randint(0, 2)
    computer_choice = ''

    if computer_action == 0:
        computer_choice = rock
    elif computer_action == 1:
        computer_choice = paper
    elif computer_action == 2:
        computer_choice = scissors
    print(f'Your opponent chose {computer_choice}')
    print()
    game_counter += 1
    if player_action == 'Rock' and computer_choice == 'Scissors' or player_action == 'Paper' and computer_choice == \
            'Rock' or \
            player_action == 'Scissors' and computer_choice == 'Paper':
        player_points += 3
        print('You win!')
        print('You get 3 points!')
        print()
    elif player_action == computer_choice:
        player_points += 1
        computer_points += 1
        print('Draw!')
        print('You get 1 points!')
        print()
    else:
        computer_points += 3
        print('You lose!')
        print()

    print(f'You have {player_points} points at the moment')
    print(f'Your opponent has {computer_points} points at the moment')
    print()
    
if player_points > computer_points:
    print('Congratulations! You Won The World Cup!')
    print(f'The winner between {favorite_team} --> {player_points} points and {computer_team} --> {computer_points} points. is {favorite_team}')
 
elif player_points == computer_points:
    print(f'The final result is draw. You have {player_points} points and your opponent has {computer_points} ')
    print(f'You have to play once again if you want to be a champion.')
else:
    print('I am sorry, but you lose the final of The World Cup!!!')
    print(f'The winner between {computer_team} --> {computer_points} points and {favorite_team} --> {player_points} points is {computer_team}')
