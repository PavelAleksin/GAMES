# 1.Позиции для х и о
# 2.Убедиться что доска пустая
# 3.Убедиться что игра работает при заняятой ячейке


theBoards = {'7':'','8':'','9':'',
             '4':'','5':'5','6':'',
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

    turn='X'
    count = 0
    
    for i in range(10):
        printBoard(theBoards)
        print(f'Первым ходит{turn}')

        move = input()
        if theBoards[move] == '':
            theBoards[move] = turn
            count+=1
        else:
            print('Ячейка занята, выбери другую')
            continue
        if count >= 5:
            if theBoards['7'] == theBoards['8'] == theBoards['9'] !='':
                printBoard(theBoards)
                print('Game Over')
                print(f'Player {turn} WIN!')
                break
            if theBoards['4'] == theBoards['5'] == theBoards['6'] !='':
                printBoard(theBoards)
                print('Game Over')
                print(f'Player {turn} WIN!')
                break

            if theBoards['1'] == theBoards['2'] == theBoards['3'] !='':
                printBoard(theBoards)
                print('Game Over')
                print(f'Player {turn} WIN!')
                break
            
            if theBoards['1'] == theBoards['5'] == theBoards['9'] !='':
                printBoard(theBoards)
                print('Game Over')
                print(f'Player {turn} WIN!')
                break
            if theBoards['3'] == theBoards['5'] == theBoards['7'] !='':
                printBoard(theBoards)
                print('Game Over')
                print(f'Player {turn} WIN!')
                break
    





