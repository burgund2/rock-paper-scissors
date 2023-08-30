#  rock-paper-scissors game
from lang_en import english_game
from lang_pl import polish_game


def print_score(score: dict[str, int], counter: int, lang: int):

    winner = [key for key in score]
    points = [val for val in score.values()]

    if lang == 1:
        print(f'\n      --- Wygrywa {winner[0]} ---')
        print(f'   Wykorzystano {counter} prób, by zdobyć {points[0]} punkty(ów)')

    else:
        print(f'\n      --- The Winner is {winner[0]} ---')
        print(f'    You needed {counter} tries to win {points[0]} points')


def main():
    while True:
        print()
        print('Main Menu:')
        print('1. Polski')
        print('2. English')
        print('0. Koniec / Exit')
        print()
        lang = int(input('Podaj język gry / Enter game language: '))

        if lang == 1:
            max_points = int(input('Do ilu wygranych punktów gramy?: '))
            score, counter = polish_game(max_points)
            print_score(score, counter, lang)
        elif lang == 2:
            max_points = int(input('Until how many points are won?: '))
            score, counter = english_game(max_points)
            print_score(score, counter, lang)
        elif lang == 0:
            print('Bye, bye ;-) ')
            break
        else:
            print('Nieprawidłowa wartość / Wrong value')
            continue


if __name__ == '__main__':
    main()
