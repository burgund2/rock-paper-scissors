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
                case [1, 2]:
                    paper_over_rock = True
                    point2 += 1
                case [2, 1]:
                    paper_over_rock = True
                    point1 += 1
                case [1, 3]:
                    rock_over_scissors = True
                    point1 += 1
                case [3, 1]:
                    rock_over_scissors = True
                    point2 += 1
                case [2, 3]:
                    scissors_over_paper = True
                    point2 += 1
                case [3, 2]:
                    scissors_over_paper = True
                    point1 += 1
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
        case [True, False, False]: print('\nPaper over Rock')
        case [False, True, False]: print('\nRock over Scissors')
        case [False, False, True]: print('\nScissors over Rock')

    print(f'Ranking: Gamer 1 - {point1} point(s), Gamer 2 - {point2} point(s)')
