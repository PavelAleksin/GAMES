# 1.Изменяем номер от 1 до 1 миллиона
# 2.Игра должна просить нас угадать число
# 3.Игра должна давать подсказку
# 4.Сообщение о победе

from  random  import randint
def game1():
    start = randint(1,100)
    end = randint(1,10000)

    values = randint(start,end)

    print(f'Число выбрано! значение между {start} и {end}. Пора угадывать =)')

    guess = None

    while guess != values:
        guess = input('Введите число: ')
        if guess == 'Exit':
            print(f'Ты сдался? бывает, а число было {values}')
            break
        guess = int(guess)
        if guess < values:
            print(f'Число больше {guess}')
        elif guess > values:
            print(f'Число меньше {guess}')
        elif guess==values:
            print(f'Поздравляем ты угадал число {values}')
    
 game1()