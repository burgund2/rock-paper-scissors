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
        gamer1 = int(getpass('Gracz nr 1 - Wybierz 1, 2 lub 3: '))
        gamer2 = int(getpass('Gracz nr 2 - Wybierz 1, 2 lub 3: '))

        if gamer1 > 3 or gamer2 > 3 or gamer1 < 1 or gamer2 < 1:
            print('\nWprowadź poprawne wartości 1, 2 lub 3 !!')
        elif gamer1 == 1 and gamer2 == 2:
            print('\nPunkt dla Gracza 1 - Papier nad Kamień')
            point1 += 1
        elif gamer1 == 1 and gamer2 == 3:
            print('\nPunkt dla Gracza nr 2 - Nożyce nad Papier')
            point2 += 1
        elif gamer1 == 2 and gamer2 == 1:
            print('\nPunkt dla Gracza nr 2 - Papier nad Kamień')
            point2 += 1
        elif gamer1 == 2 and gamer2 == 3:
            print('\nPunkt dla Gracza nr 1 - Kamień nad Nożyce')
            point1 += 1
        elif gamer1 == 3 and gamer2 == 1:
            print('\nPunkt dla Gracza nr 1 - Nożyce nad Papier')
            point1 += 1
        elif gamer1 == 3 and gamer2 == 2:
            print('\nPunkt dla Gracza nr 2 - Kamień nad Nożyce')
            point2 += 1
        elif gamer1 == 1 and gamer2 == 1:
            print('\nNie przyznano punktów: Papier = Papier')
        elif gamer1 == 2 and gamer2 == 2:
            print('\nNie przyznano punktów: Kamień = Kamień')
        else:
            print('\nNie przyznano punktów: Nożyce = Nożyce')

        print(f'Ranking: Gracz 1 - {point1} punkt(ów), Gracz 2 - {point2} punkt(ów)')
        counter += 1
        if point1 == max_points:
            print('      --- Wygrywa Gracz nr 1 ---')
            print(f'     Wykorzystano {counter} prób aby zdobyć {max_points} punktów')
            break
        elif point2 == max_points:
            print('      --- Wygrywa Gracz nr 2 ---')
            print(f'     Wykorzystano {counter} prób aby zdobyć {max_points} punktów')
            break
