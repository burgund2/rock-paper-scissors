#  rock-paper-scissors game
from lang_en import english_game
from lang_pl import polish_game


if __name__ == '__main__':
    while True:
        print()
        print('Main Menu:')
        print('1. Polski')
        print('2. English')
        print('0. Koniec / Exit')
        print()
        answer = int(input('Podaj język gry / Enter game language: '))

        if answer == 1:
            max_points = int(input('Do ilu wygranych punktów gramy?: '))
            polish_game(max_points)
        elif answer == 2:
            max_points = int(input('Until how many points are won?: '))
            english_game(max_points)
        elif answer == 0:
            print('Bye, bye ;-) ')
            break
        else:
            print('Nieprawidłowa wartość / Wrong value')
            continue
