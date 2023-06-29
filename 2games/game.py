# 1.Позиции для х и о
# 2.Убедиться что доска пустая
# 3.Убедиться что игра работает при заняятой ячейке
import os
import sys

theBoards = {'7':'','8':'','9':'',
             '4':'','5':'','6':'',
             '1':'','2':'','3':''}


boardKeys=[]

for key in theBoards:
    boardKeys.append(key)

def printBoard(board):
    
    print(board['7'] + '    |' + board['8'] + '    |' + board['9'])
    print('----|----|----')

    print(board['4'] + '    |' + board ['5'] + '    |' + board['6'])
    print('----|----|----')

    print(board['1'] + '    |' + board['2'] + '    |' + board['3'])

def game():
    os.system('CLS')
    for key in theBoards:
        theBoards[key]=''
    turn='X'
    count = 0
    move = 777
    for i in range(1000):
        printBoard(theBoards)
        print(f'Сейчас ход игрока: {turn}')

        move = input(f'Выбирай клетку игрок {turn}: ')
        os.system('CLS')
        try:
            if move == 'ex':
                sys.exit(1)
            elif theBoards[move] == '':
                theBoards[move] = turn
                count+=1
            else:
                print('Ячейка занята, выбери другую!')
                count = count
                continue
        except KeyError:
            print ("Ошибка! Введено пустое или неверное значение. Выберите значение от 1 до 9.Повторите ход. Для выхода введите 'ex' ")
            continue
        if count >= 5:
            if     theBoards['7'] == theBoards['8'] == theBoards['9'] != '' \
                or theBoards['4'] == theBoards['5'] == theBoards['6'] != ''\
                or theBoards['1'] == theBoards['2'] == theBoards['3'] != ''\
                or theBoards['1'] == theBoards['4'] == theBoards['7'] != ''\
                or theBoards['2'] == theBoards['5'] == theBoards['8'] != ''\
                or theBoards['3'] == theBoards['6'] == theBoards['9'] != ''\
                or theBoards['1'] == theBoards['5'] == theBoards['9'] != ''\
                or theBoards['7'] == theBoards['5'] == theBoards['3'] != '':
                print('Game Over')
                print(f'Player {turn} WIN!')
                break
            elif count == 9:
                print('Ничья')
                break
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'


    restart = input('Повторим? Введи зачение \'y\' или нажмите ENTER для завершения игры: ')
    if restart == 'y' or restart == 'Y':
        for key in theBoards:
            theBoards[key] = ''
        game()
    else:
        sys.exit(1)

if __name__=='__main__':
    game()




