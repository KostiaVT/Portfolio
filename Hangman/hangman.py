import random

def hangman():
    print ('Привет! Добро пожаловать в игру Виселица')
    print ('Угадайте игру')
    wordlist = ['футбол', 'хоккей', 'теннис', 'баскетбол']
    secret = random.choice(wordlist)
    guesses = 'ауоыиэяюеё'
    turns = 5
    while turns > 0:
        missed = 0
        for letter in secret:
            if letter in guesses:
                print (letter,end=' ')
            else:
                print (' ',end=' ')
                missed += 1
        if missed == 0:
            print ('\nТы выиграл')
            break

        guess = input('\nНазовите букву: ')
        guesses += guess

        if guess not in secret:
            turns -= 1
            print ('\Не угадал')
            print ('\n', 'Осталось попыток: ', turns)
            if turns < 5: print('\n  |  ')
            if turns < 4: print('  o  ')
            if turns < 3: print(" /|\ ")
            if turns < 2: print('  |  ')
            if turns < 1: print(' /\ ')
            if turns == 0: print('\n\nЭто слово: ', secret)

ans = 'да'
while ans == 'да':
    hangman()
    print('Хочешь сыграть снова? (да или нет)')
    ans = input()
