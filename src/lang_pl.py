from getpass import getpass


def polish_game(max_points):
    point1 = 0
    point2 = 0
    counter = 0
    while True:
        print()
        print("Menu:")
        print('1. Papier')
        print('2. Kamień')
        print('3. Nożyce')
        print()
        gamer1_choice = int(getpass('Gracz nr 1 - Wybierz 1, 2 lub 3: '))
        gamer2_choice = int(getpass('Gracz nr 2 - Wybierz 1, 2 lub 3: '))

        paper_over_rock = False
        rock_over_scissors = False
        scissors_over_paper = False
        if gamer1_choice > 3 or gamer2_choice > 3 or gamer1_choice < 1 or gamer2_choice < 1:
            print('\nWprowadź poprawne wartości 1, 2 lub 3 !!')
        elif gamer1_choice == 1 and gamer2_choice == 2:
            paper_over_rock = True
            point1 += 1
        elif gamer1_choice == 1 and gamer2_choice == 3:
            scissors_over_paper = True
            point2 += 1
        elif gamer1_choice == 2 and gamer2_choice == 1:
            paper_over_rock = True
            point2 += 1
        elif gamer1_choice == 2 and gamer2_choice == 3:
            rock_over_scissors = True
            point1 += 1
        elif gamer1_choice == 3 and gamer2_choice == 1:
            scissors_over_paper = True
            point1 += 1
        elif gamer1_choice == 3 and gamer2_choice == 2:
            rock_over_scissors = True
            point2 += 1
        elif gamer1_choice == 1 and gamer2_choice == 1:
            print('\nNie przyznano punktów: Papier = Papier')
        elif gamer1_choice == 2 and gamer2_choice == 2:
            print('\nNie przyznano punktów: Kamień = Kamień')
        else:
            print('\nNie przyznano punktów: Nożyce = Nożyce')

        if paper_over_rock:
            print('\n- Papier ponad Kamień -')
        elif rock_over_scissors:
            print('\n- Kamień ponad Nożyce -')
        elif scissors_over_paper:
            print('\n- Nożyce ponad Papier -')

        print(f'Ranking: Gracz 1 - {point1} punkt(ów), Gracz 2 - {point2} punkt(ów)')
        counter += 1

        score = {}
        if point1 == max_points:
            score['Gracz 1'] = max_points
            break
        elif point2 == max_points:
            score['Gracz 2'] = max_points
            break

    return score, counter
