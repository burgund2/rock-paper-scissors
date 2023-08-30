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

        if gamer1_choice > 3 or gamer2_choice > 3 or gamer1_choice < 1 or gamer2_choice < 1:
            print('\nWprowadź poprawne wartości 1, 2 lub 3 !!')
        elif gamer1_choice == 1 and gamer2_choice == 2:
            print('\nPunkt dla Gracza 1 - Papier nad Kamień')
            point1 += 1
        elif gamer1_choice == 1 and gamer2_choice == 3:
            print('\nPunkt dla Gracza nr 2 - Nożyce nad Papier')
            point2 += 1
        elif gamer1_choice == 2 and gamer2_choice == 1:
            print('\nPunkt dla Gracza nr 2 - Papier nad Kamień')
            point2 += 1
        elif gamer1_choice == 2 and gamer2_choice == 3:
            print('\nPunkt dla Gracza nr 1 - Kamień nad Nożyce')
            point1 += 1
        elif gamer1_choice == 3 and gamer2_choice == 1:
            print('\nPunkt dla Gracza nr 1 - Nożyce nad Papier')
            point1 += 1
        elif gamer1_choice == 3 and gamer2_choice == 2:
            print('\nPunkt dla Gracza nr 2 - Kamień nad Nożyce')
            point2 += 1
        elif gamer1_choice == 1 and gamer2_choice == 1:
            print('\nNie przyznano punktów: Papier = Papier')
        elif gamer1_choice == 2 and gamer2_choice == 2:
            print('\nNie przyznano punktów: Kamień = Kamień')
        else:
            print('\nNie przyznano punktów: Nożyce = Nożyce')

        score = {}
        print(f'Ranking: Gracz 1 - {point1} punkt(ów), Gracz 2 - {point2} punkt(ów)')
        counter += 1

        if point1 == max_points:
            score['Gracz 1'] = max_points
            break
        elif point2 == max_points:
            score['Gracz 2'] = max_points
            break

    return score, counter
