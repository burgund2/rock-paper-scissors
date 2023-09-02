from getpass import getpass


def english_game(max_points):
    point1 = 0
    point2 = 0
    counter = 0
    while True:
        paper_over_rock = False
        rock_over_scissors = False
        scissors_over_paper = False

        print()
        print("Menu:")
        print('1. Rock')
        print('2. Paper')
        print('3. Scissors')
        print()
        try:
            gamer1_choice = int(getpass('Gamer 1 - Select 1, 2 or 3: '))
            gamer2_choice = int(getpass('Gamer 2 - Select 1, 2 or 3: '))

            gamers_choice = [gamer1_choice, gamer2_choice]
            match gamers_choice:
                case [1, 2] | [2, 1]:
                    paper_over_rock = True
                    if gamer1_choice == 2:
                        point1 += 1
                    else:
                        point2 += 1
                case [1, 3] | [3, 1]:
                    rock_over_scissors = True
                    if gamer1_choice == 1:
                        point1 += 1
                    else:
                        point2 += 1
                case [2, 3] | [3, 2]:
                    scissors_over_paper = True
                    if gamer1_choice == 3:
                        point1 += 1
                    else:
                        point2 += 1
                case [1, 1]:
                    choice = 'Rock'
                    print(f'\nNo points awarded: {choice} = {choice}')
                case [2, 2]:
                    choice = 'Paper'
                    print(f'\nNo points awarded: {choice} = {choice}')
                case [3, 3]:
                    choice = 'Scissors'
                    print(f'\nNo points awarded: {choice} = {choice}')
                case _:
                    print('\nEnter valid value 1, 2 or 3 !!')
        except ValueError:
            print('Value must be a digit !!')

        print_ranking(point1, point2, paper_over_rock,
                      rock_over_scissors, scissors_over_paper)
        counter += 1

        score = {}
        if point1 == max_points:
            score['Gamer 1'] = max_points
            break
        elif point2 == max_points:
            score['Gamer 2'] = max_points
            break

    return score, counter


def print_ranking(point1, point2, paper_over_rock=False,
                  rock_over_scissors=False, scissors_over_paper=False):

    type_of_choices = [paper_over_rock, rock_over_scissors, scissors_over_paper]  # noqa: E501

    match type_of_choices:
        case [True, False, False]: print('\nPapier nad Kamień')
        case [False, True, False]: print('\nKamień nad Nożyce')
        case [False, False, True]: print('\nNożyce nad Papier')

    print(f'Ranking: Gamer 1 - {point1} point(s), Gamer 2 - {point2} point(s)')
