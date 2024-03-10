import tkinter as tk
import random
import winsound

KURO=1
SIRO=2


cursor_x=0
cursor_y=0
mouse_x=0
mouse_y=0
mouse_c=0
stone=True #True:黒 False:白

def mouse_move(e):
  global mouse_x,mouse_y
  mouse_x=e.x
  mouse_y=e.y


def mouse_press(e):
  global mouse_c
  mouse_c=1

board=[]
check=[]

for i in range(8):
  board.append([0,0,0,0,0,0,0,0])
  check.append([0,0,0,0,0,0,0,0])



def init_board():
  for y in range(8):
    for x in range(8):
      board[y][x]=0
  
  board[3][3]=1 
  board[3][4]=2 
  board[4][3]=2
  board[4][4]=1

  stone=True

def draw_board():
  cvs.delete("STONE")
  for y in range(8):
    for x in range(8):
      if board[y][x]>0:
        if board[y][x]==1:
          cvs.create_oval((185+27.1875+x*54.375)-20,(80+27.1875+y*54.375)-20,(185+27.1875+x*54.375)+20,(80+27.1875+y*54.375)+20,fill="black",tag="STONE")
        if board[y][x]==2:
          cvs.create_oval((185+27.1875+x*54.375)-20,(80+27.1875+y*54.375)-20,(185+27.1875+x*54.375)+20,(80+27.1875+y*54.375)+20,fill="white",outline="black",width=1,tag="STONE")

def pos1(cursor_x,cursor_y,stone): 
  ctn=0
  for x in range(cursor_x-1,0,-1):
      if board[cursor_y][x]==2:
        cnt=cnt+1
      if board[cursor_y][x]==1:
        if ctn>0:
          return True
        else:
          return False
      if board[cursor_y][x]==0:
        return False
def pos2(cursor_x,cursor_y,stone):
      cnt=0
      for x in range(cursor_x+1,8):
        if board[cursor_y][x]==2:
          cnt=cnt+1
        if board[cursor_y][x]==1:
          if cnt>0:
            return True
          else:
            return False
        if board[cursor_y][x]==0:
          return False

def pos3(cursor_x,cursor_y,stone):  
      cnt=0
      for y in range(cursor_y+1,8):
        if board[y][cursor_x]==2:
          cnt=cnt+1
        if board[y][cursor_x]==1:
          if cnt>0:
            return True
          else:
            return False
        if board[y][cursor_x]==0:
          return False
def pos4(cursor_x,cursor_y,stone):
    cnt=0
    for y in range(1,8):
      if cursor_x-y<0 or cursor_y-y<0:
        break
      if board[cursor_y-y][cursor_x-y]==2:
        cnt=cnt+1
      if board[cursor_y-y][cursor_x-y]==1:
        if cnt>0:
          return True
        else:
          return False
  
def pos5(cursor_x,cursor_y,stone):
  ctn=0
  for y in range(cursor_y-1,0,-1):
      for x in range(cursor_x-1,0,-1):
        if board[y][x]==2:
          cnt=cnt+1
        if board[y][x]==1:
          if cnt>0:
            return True
          else:
            return False
        if board[y][x]==0:
          return False
def pos6(cursor_x,cursor_y,stone):
    cnt=0
    for y in range(cursor_y+1,8):
      for x in range(cursor_x+1,8):
        if board[y][x]==2:
          cnt=cnt+1
        if board[y][x]==1:
          if cnt>0:
            return True
          else:
            return False
        if board[y][x]==0:
          return False
def pos7(cursor_x,cursor_y,stone):
    cnt=0
    for y in range(cursor_y-1,0,-1):
      for x in range(cursor_x+1,8):
        if board[y][x]==2:
          cnt=cnt+1
        if board[y][x]==1:
          if cnt>0:
            return True
          else:
            return False
        if board[y][x]==0:
          return False
def pos8(cursor_x,cursor_y,stone):
    cnt=0
    for y in range(cursor_y+1,8):
      for x in range(cursor_x-1,0,-1):
        if board[y][x]==2:
          cnt=cnt+1
        if board[y][x]==1:
          if cnt>0:
            return True
          else:
            return False
        if board[y][x]==0:
          return False
   
 
      

  




def put_stone():
  global cursor_x,cursor_y
  cursor_x=(mouse_x-185)//54.375
  cursor_y=(mouse_y-80)//54.375
  if mouse_c==1 and cursor_x>=0 and cursor_x<8 and cursor_y>=0 and cursor_y<8:
    if board[cursor_y][cursor_x]==0 and pos(cursor_x,cursor_y,stone)==True:
      board[cursor_y][cursor_x]=1 if stone==True else 2
      draw_board()
      sound2()

def chaeck_board(cursor_x,cursor_y,stone):
  for y in range(8):
    for x in range(8):
      check[y][x]=board[y][x]

  if stone==True:  
    ctn=0
    for x in range(cursor_x-1,0,-1):
      if board[cursor_y][x]==2:
        cnt=cnt+1
      if board[cursor_y][x]==1:
        if ctn>0:
          return True
        else:
          return False
      if board[cursor_y][x]==0:
        return False
      

def sound1_cahru(): #開始時の音
  winsound.Beep(261,100)
  winsound.Beep(293,100)
  winsound.Beep(329,700)
  winsound.Beep(293,100)
  winsound.Beep(261,700)
  winsound.Beep(261,100)
  winsound.Beep(293,100)
  winsound.Beep(329,100)
  winsound.Beep(293,100)
  winsound.Beep(261,100)
  winsound.Beep(293,700)

def sound2(): #石を置いたときの音
  winsound.Beep(329,100)

def sound3_happy(): #勝利時の音
  winsound.Beep(440,300)
  winsound.Beep(440,300)
  winsound.Beep(440,300)
  winsound.Beep(392,200)
  winsound.Beep(440,600)
  winsound.Beep(349,800)

def sound3_destiny(): #敗北時の音
  winsound.Beep(392,300)
  winsound.Beep(392,300)
  winsound.Beep(392,300)
  winsound.Beep(310,1000)
  winsound.Beep(349,300)
  winsound.Beep(349,300)
  winsound.Beep(349,300)
  winsound.Beep(293,1000)  

root=tk.Tk()

root.title("オセロ対戦")
root.resizable(False,False)
cvs=tk.Canvas(width=800,height=600)
cvs.pack()
root.bind("<Motion>",mouse_move)
root.bind("<ButtonPress>",mouse_press)
bg=tk.PhotoImage(file="board.png")
cvs.create_image(400,300,image=bg)
init_board()
draw_board()
sound3_destiny()
root.after(100,)
root.mainloop()