from getpass import getpass


def english_game(max_points):
    point1 = 0
    point2 = 0
    counter = 0
    while True:
        print()
        print("Menu:")
        print('1. Rock')
        print('2. Paper')
        print('3. Scissors')
        print()
        gamer1 = int(getpass('Gamer nr 1 - Select 1, 2 or 3: '))
        gamer2 = int(getpass('Gamer nr 2 - Select 1, 2 or 3: '))

        if gamer1 > 3 or gamer2 > 3 or gamer1 < 1 or gamer2 < 1:
            print('\nEnter valid value 1, 2 or 3 !!')
        elif gamer1 == 2 and gamer2 == 1:
            print('\nPoint for Gamer 1 - Paper over Rock')
            point1 += 1
        elif gamer1 == 2 and gamer2 == 3:
            print('\nPoint for Gamer 2 - Scissors over Paper')
            point2 += 1
        elif gamer1 == 1 and gamer2 == 2:
            print('\nPoint for Gamer 2 - Paper over Rock')
            point2 += 1
        elif gamer1 == 1 and gamer2 == 3:
            print('\nPoint for Gamer 1 - Rock over Scissors')
            point1 += 1
        elif gamer1 == 3 and gamer2 == 2:
            print('\nPoint for Gamer 1 - Scissors over Paper')
            point1 += 1
        elif gamer1 == 3 and gamer2 == 1:
            print('\nPoint for Gamer 2 - Rock over Scissors')
            point2 += 1
        elif gamer1 == 1 and gamer2 == 1:
            print('\nNo points awarded: Paper = Paper')
        elif gamer1 == 2 and gamer2 == 2:
            print('\nNo points awarded: Rock = Rock')
        else:
            print('\nNo points awarded: Scissors = Scissors')

        print(f'Ranking: Gamer 1 - {point1} point(s), Gamer 2 - {point2} point(s))')
        counter += 1
        if point1 == max_points:
            print('      --- The Winner is Gamer 1 ---')
            print(f'    You needed {counter} tries to win {max_points} points')
            break
        elif point2 == max_points:
            print('      --- The Winner is Gamer 2 ---')
            print(f'    You needed {counter} tries to win {max_points} points')
            break
