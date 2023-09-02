from getpass import getpass


def polish_game(max_points):
    point1 = 0
    point2 = 0
    counter = 0
    while True:
        paper_over_rock = False
        rock_over_scissors = False
        scissors_over_paper = False

        print()
        print("Menu:")
        print('1. Papier')
        print('2. Kamień')
        print('3. Nożyce')
        print()
        try:
            gamer1_choice = int(getpass('Gracz nr 1 - Wybierz 1, 2 lub 3: '))
            gamer2_choice = int(getpass('Gracz nr 2 - Wybierz 1, 2 lub 3: '))

            gamers_choice = [gamer1_choice, gamer2_choice]
            match gamers_choice:
                case [1, 2]:
                    paper_over_rock = True
                    point1 += 1
                case [2, 1]:
                    paper_over_rock = True
                    point2 += 1
                case [2, 3]:
                    rock_over_scissors = True
                    point1 += 1
                case [3, 2]:
                    rock_over_scissors = True
                    point2 += 1
                case [1, 3]:
                    scissors_over_paper = True
                    point2 += 1
                case [3, 1]:
                    scissors_over_paper = True
                    point1 += 1
                case [1, 1]:
                    choice = 'Papier'
                    print(f'\nNie przyznano punktów: {choice} = {choice}')
                case [2, 2]:
                    choice = 'Kamień'
                    print(f'\nNie przyznano punktów: {choice} = {choice}')
                case [3, 3]:
                    choice = 'Nożyce'
                    print(f'\nNie przyznano punktów: {choice} = {choice}')
                case _:
                    print('\nWprowadź poprawne wartości 1, 2 lub 3 !!')
        except ValueError:
            print('Wartość musi być cyfrą !!')

        print_ranking(point1, point2, paper_over_rock,
                      rock_over_scissors, scissors_over_paper)
        counter += 1

        score = {}
        if point1 == max_points:
            score['Gracz 1'] = max_points
            break
        elif point2 == max_points:
            score['Gracz 2'] = max_points
            break

    return score, counter


def print_ranking(point1, point2, paper_over_rock=False,
                  rock_over_scissors=False, scissors_over_paper=False):

    type_of_choices = [paper_over_rock, rock_over_scissors, scissors_over_paper]  # noqa: E501

    match type_of_choices:
        case [True, False, False]: print('\nPapier nad Kamień')
        case [False, True, False]: print('\nKamień nad Nożyce')
        case [False, False, True]: print('\nNożyce nad Papier')

    print(f'Ranking: Gracz 1 - {point1} punkt(ów), Gracz 2 - {point2} punkt(ów)')  # noqa: E501
