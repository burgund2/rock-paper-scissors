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
        gamer1_choice = int(getpass('Gamer 1 - Select 1, 2 or 3: '))
        gamer2_choice = int(getpass('Gamer 2 - Select 1, 2 or 3: '))

        paper_over_rock = False
        rock_over_scissors = False
        scissors_over_paper = False
        if gamer1_choice > 3 or gamer2_choice > 3 \
                or gamer1_choice < 1 or gamer2_choice < 1:
            print('\nEnter valid value 1, 2 or 3 !!')

        elif gamer1_choice == 1 and gamer2_choice == 2 \
                or gamer1_choice == 2 and gamer2_choice == 1:
            paper_over_rock = True
            if gamer1_choice == 1:
                point1 += 1
            else:
                point2 += 1

        elif gamer1_choice == 2 and gamer2_choice == 3 \
                or gamer1_choice == 3 and gamer2_choice == 2:
            rock_over_scissors = True
            if gamer1_choice == 2:
                point1 += 1
            else:
                point2 += 1

        elif gamer1_choice == 3 and gamer2_choice == 1 \
                or gamer1_choice == 1 and gamer2_choice == 3:
            scissors_over_paper = True
            if gamer1_choice == 3:
                point1 += 1
            else:
                point2 += 1

        else:
            if gamer1_choice == 1:
                choice = 'Rock'
            elif gamer1_choice == 2:
                choice = 'Paper'
            else:
                choice = 'Scissors'
            print(f'\nNo points awarded: {choice} = {choice}')

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

    if paper_over_rock:
        print('\n- Paper over Rock -')
    elif rock_over_scissors:
        print('\n- Rock over Scissors -')
    elif scissors_over_paper:
        print('\n- Scissors over Paper -')
    print(f'Ranking: Gamer 1 - {point1} point(s), Gamer 2 - {point2} point(s)')
