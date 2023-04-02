import random
import datetime
today = datetime.date.today()
year = today.year

list_of_countries = ['Argentina', 'Brazil', 'Bulgaria', 'China', 'Denmark', 'Egypt', 'France', 'Germany', 'Hungary',
                     'Italy', 'Poland', 'South Africa', 'Uruguay', 'Paraguay', 'South Korea', 'Japan', 'Czech Republic',
                     'Jamaica', 'Morocco', 'Latvia', 'Mexico', 'Netherlands', 'Nigeria', 'Portugal', 'Qatar', 'Russia',
                     'Spain', 'Turkey', 'Ukraine', 'Venezuela', 'Cameron', 'Romania']

symbols = ['✋🏻', '✊🏻', '✌️🏻️']
home = random.choice(list_of_countries)

print(f'Welcome to World Cup {home} {year}')
print()

player_team = random.choice(list_of_countries)
print(f"Your Team is {player_team}.")

list_of_countries.remove(player_team)
print('---------------------------')

computer_team = random.choice(list_of_countries)
print(f"Opponent's Team is {computer_team}.")
print()

rock = '✊🏻'
paper = '✋🏻'
scissors = '✌️🏻️'

player_points = 0
computer_points = 0

while True:
    if player_points >= 10 or computer_points >= 10:
        break

    player_choice = input("Please Choose [r]ock, [p]aper or [s]cissors: ").lower()

    if player_choice == "r":
        player_choice = rock
    elif player_choice == "p":
        player_choice = paper
    elif player_choice == "s":
        player_choice = scissors
    else:
        print("Invalid Input. Try again...")
        continue

    computer_choice = random.choice(symbols)

    print(f'{player_team} choose {player_choice}')
    print(f'{computer_team} choose {computer_choice}')
    print()

    if player_choice == rock and computer_choice == scissors or player_choice == paper and computer_choice == \
            rock or \
            player_choice == scissors and computer_choice == paper:
        player_points += 3
        print(f'{player_team} win!')
        print()
    elif player_choice == computer_choice:
        player_points += 1
        computer_points += 1
        print('Draw!')
        print()
    else:
        computer_points += 3
        print(f'{computer_team} win!')
        print()

    print(f'Current Result:')
    print(f'{player_team}: {player_points}')
    print(f'{computer_team}: {computer_points}')
    print()

if player_points > computer_points:
    print(f'Congratulations! You Won The World Cup {home} {year}!')
    print(f'The winner between {player_team} {player_points} points and {computer_team} {computer_points} points. is {player_team}!')
else:
    print(f'I am sorry, but you lose the final of The World Cup {home} {year}!')
    print(f'The winner between {computer_team} {computer_points} points and {player_team} {player_points} points is {computer_team}!')
