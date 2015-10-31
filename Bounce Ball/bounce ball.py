#Bounce Ball  1.1
from tkinter import *
import random
import time


class Ball:     #创建球的分类
    def __init__(self,canvas,paddle,color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25,fill=color)#创建球的大小颜色
        self.canvas.move(self.id,245,100)#球的初始位置
        starts = [-3,-2,-1,1,2,3] 
        random.shuffle(starts)#随机速度与方向
        self.x= starts[0]        
        self.y= -3
        self.canvas_height = self.canvas.winfo_height()#读取当前位置
        self.canvas_width = self.canvas.winfo_width()#读取当前位置
        self.hit_bottom = False
        
    def hit_paddle(self,pos): #判断是否碰到挡板
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0]<= paddle_pos[2]:
            '''判断横坐标
               pos[2]是球的右端点 paddle_pos[0]是挡板左端点'''
            if pos[3] >= paddle_pos[1] and pos[1]<= paddle_pos[3]:#判断纵坐标
                return True
            return False
    
    def draw(self): #画出图像并且更新坐标
        self.canvas.move(self.id,self.x,self.y)# x表示横向移动 y表示纵向移动
        pos = self.canvas.coords(self.id)#读取当前球的上下左右坐标
        if pos[1]<= 0: # 球的顶部高度
            self.y = 3 # 更新方向速度
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0]<= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x =0
        self.canvas_width = self.canvas.winfo_width()#读取宽度以便判断hit
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)#键盘操作
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)#键盘操作

    def draw(self): #画出图像并且更新坐标
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:#判断是否碰到左右屏幕
            self.x = 0 #如果碰到就停下  设置成-1可变成反弹
        elif pos[2]>= self.canvas_width:
            self.x =0
    
    def turn_left(self,evt):#导入键盘操作效果
        self.x =-3  #速度可调节
    def turn_right(self,evt):
        self.x =3

def START(): # 按钮的功能
    while 1:
        if ball.hit_bottom == False: #如果按钮时游戏没有结束 就开始游戏
            ball.draw()
            paddle.draw()
        tk.update_idletasks()
        tk.update()#实时更新
        time.sleep(0.01)#更新间隔
        if ball.hit_bottom == True:
            canvas.create_text(250,200,text='GAME OVER!!')
            break #加break可以解决关闭窗口后报错 但是无法重开游戏

tk= Tk()  #面向对象
tk.title("Game") #标题
tk.resizable(0,0)#固定窗口大小
tk.wm_attributes("-topmost",0)#窗口置顶
canvas = Canvas(tk,width=500,height=400,bd=0, highlightthickness=0)#设定窗口大小边框
canvas.pack()#生成窗口
btn =Button(tk,text='game start',command =START)#设定按钮
btn.pack()#生成按钮
tk.update()#更新对象

paddle = Paddle(canvas,'blue') #设定挡板参数
ball = Ball(canvas,paddle,'red')#设定小球参数


