# number_a = int(input('Первое значение:' ))
# number_b = int(input('Второе значение:' ))
# sub = number_b-number_a
# print('Рeзультат: ' + str(sub))

class line:
    def __init__(self,length,x,y):
        self.length = length
        self.x = x
        self.y =y
    def draw(self):
        print('Drawing...')
    def display(self):
        print('Display')

line1 = line(5,1,1)

print(line1.length)

line1.draw()
line1.display()