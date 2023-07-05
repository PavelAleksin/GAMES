import tkinter as tk



class PlayComponent(object):
    def __init__(self,canvas,item):
        self.item = item
        self.canvas = canvas

    def move(self,x,y):
        self.canvas.move(self.item,x,y)

    def position(self):
        return self.canvas.coords(self.item)

    def delete(self):
        self.canvas.dele(self.item)


class Paddle(PlayComponent):
    def __init__(self, canvas, x,y):
        self.height = 10
        self.width = 100
        self.ball = None
        item = canvas.create_rectangle(x-self.width/2,
                                       y-self.height/2,
                                       x+self.width/2,
                                       y+self.height/2,
                                       fill = 'White') 
        super(Paddle,self).__init__(canvas,item)

    def set_ball(self,ball):
        self.ball = ball
    
    def move(self,dist):
        coord = self.position()
        width = self.canvas.winfo_width()
        if coord[2]+dist <= width and coord[0] + dist>=0:
            super(Paddle,self).move(dist,0)
            if self.ball is not None:
                self.ball.move(dist,0)

class Brick(PlayComponent):
    colorArray = {1: 'deepskyblue', 2: 'dodgerblue',3: 'blue'}
    def __init__(self, canvas,x,y,hits):
        self.width = 60
        self.heigt = 20
        self.hits = hits
        color = Brick.colorArray[hits]
        item = canvas.create_rectangle(x-self.width/2,
                                       y-self.heigt/2,
                                       x+self.width/2,
                                       y+self.heigt/2,
                                       fill = color, tag = 'brick')
        super(Brick,self).__init__(canvas,item)


class Ball(PlayComponent):
    def __init__(self, canvas,x,y):
        self.radius = 10
        self.speed = 8
        self.direction = [-1,1]
        item = canvas.create_oval(x-self.radius,
                                  y-self.radius,
                                  x+self.radius,
                                  y+self.radius,
                                  fill= 'White')
        super(Ball,self).__init__(canvas,item)
    
    def update(self):
        coord = self.position()
        width = self.canvas.winfo_width()
        if coord[1] <= 0:
            self.direction[1]*= -1
        if coord[2] >= width or coord[0] <=0:
            self.direction[0]*= -1
        
        x = self.direction[0]*self.speed
        y = self.direction[1]*self.speed
        self.move(x,y)
 


class Game(tk.Frame):
    def __init__(self, master):
        super(Game,self).__init__(master)
        self.width = 1000;
        self.height =400;

        self.canvas = tk.Canvas(self,bg='darkorange',width= self.width,
                                height=self.height)
        
        self.canvas.pack()
        self.pack()

        self.items ={}
        self.ball = None

        self.paddle=Paddle(self.canvas, self.width/2, 320)
        self.items[self.paddle.item]=self.paddle
        
        for x in range(100,self.width - 100, 60):
            self.display_brick(x+20, 50, 2)

        self.hud =None
        self.init_game()
        self.canvas.focus_set()
        self.canvas.bind('<Left>',
                         lambda _:self.paddle.move(-20))
        self.canvas.bind('<Right>',
                         lambda _:self.paddle.move(20))


    def init_game(self):
        self.display_ball()
        self.start_game()

    def display_ball(self):
        if self.ball is not None:
            self.ball.delete()
        paddle_coords = self.paddle.position()
        x=(paddle_coords[0]+paddle_coords[2])*0.5
        self.ball = Ball(self.canvas,x,310)
        self.paddle.set_ball(self.ball)

    def display_brick(self,x,y,hits):
        brick = Brick(self.canvas,x,y,hits)
        self.item[brick.item] = brick


    def start_game(self):
        self.canvas.unbind('<space>')
        self.paddle.ball= None
    
    def game_loop(self):
        num_bricks = len(self.canvas.find_withtag('brick'))
    
        if num_bricks ==0:
            self.ball.speed = None
        else:
            self.ball.update()
            self.after(50, self.game_loop())


if __name__=='__main__':
    root=tk.Tk()
    root.title('Brick Breaker')
    game = Game(root)
    game.mainloop()
