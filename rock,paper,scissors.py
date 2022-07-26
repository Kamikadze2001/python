choise = ""
def game():
    pl1 = input('rock,paper,scissors? ')
    pl2 = input('rock,paper,scissors? ')
    if pl1 == pl2:
        print('Same choises '+pl1)
    else:
        if pl1 == 'rock' and pl2 == 'paper':
            print('Player 2 wins')
        else:
            if pl1 == 'rock' and pl2 == 'scissors':
                print('Player 1 wins')
            else:
                if pl1 == 'paper' and pl2 == 'rock':
                    print('Player 1 wins')
                else:
                    if pl1 == 'paper' and pl2 == 'scissors':
                        print('Player 2 wins')
                    else:
                        if pl1 == 'scissors' and pl2 == 'rock':
                            print('Player 2 wins')
                        else:
                            if pl1 == 'scissors' and pl2 == 'paper':
                                print('Player 1 wins')
                            else:
                                print('wrong input')
    global choise 
    choise = input('Do you want to play again Y/N? ')
    while choise == 'Y':
        game()

game()

    


