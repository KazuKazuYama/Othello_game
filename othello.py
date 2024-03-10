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

for i in range(10):
  board.append([0,0,0,0,0,0,0,0,0,0])
  check.append([0,0,0,0,0,0,0,0,0,0])



def init_board():
  for y in range(8):
    for x in range(8):
      board[y+1][x+1]=0
  for y in range(10):
    board[y][0]=-1
    board[y][9]=-1
  for x in range(10):
    board[0][x]=-1
    board[9][x]=-1
  
  board[4][4]=1 
  board[4][5]=2 
  board[5][4]=2
  board[5][5]=1

  stone=True

def draw_board():
  cvs.delete("STONE")
  for y in range(8):
    for x in range(8):
      if board[y+1][x+1]>0:
        if board[y+1][x+1]==1:
          cvs.create_oval((185+27.1875+x*54.375)-20,(80+27.1875+y*54.375)-20,(185+27.1875+x*54.375)+20,(80+27.1875+y*54.375)+20,fill="black",tag="STONE")
        if board[y+1][x+1]==2:
          cvs.create_oval((185+27.1875+x*54.375)-20,(80+27.1875+y*54.375)-20,(185+27.1875+x*54.375)+20,(80+27.1875+y*54.375)+20,fill="white",outline="black",width=1,tag="STONE")

def pos1(cursor_x,cursor_y,stone): #左
  cnt=0
  for x in range(cursor_x-1,0,-1):
    if board[cursor_y][x]==2 if stone==True else 1:
      cnt=cnt+1
    if board[cursor_y][x]==1 if stone==True else 2:
      if cnt>0:
        return True
      else:
        return False
    if board[cursor_y][x]==0 or board[cursor_y][x]==-1:
      return False
def pos2(cursor_x,cursor_y,stone): #右
  cnt=0
  for x in range(cursor_x+1,10):
    if board[cursor_y][x]==2 if stone==True else 1:
      cnt=cnt+1
      if board[cursor_y][x]==1 if stone==True else 2:
        if cnt>0:
            return True
        else:
            return False
    if board[cursor_y][x]==0 or board[cursor_y][x]==-1:
      return False

def pos3(cursor_x,cursor_y,stone):  #上
  cnt=0
  for y in range(cursor_y+1,10):
    if board[y][cursor_x]==2  if stone==True else 1:
      cnt=cnt+1
    if board[y][cursor_x]==1 if stone==True else 2:
      if cnt>0:
        return True
      else:
        return False
    if board[y][cursor_x]==0 or board[y][cursor_x]==-1:
      return False

def pos4(cursor_x,cursor_y,stone):
  cnt=0
  for y in range(cursor_y-1,0,-1): #下
    if board[y][cursor_x]==2 if stone==True else 1:
      cnt=cnt+1
    if board[y][cursor_x]==1 if stone==True else 2:
      if cnt>0:
        return True
      else:
        return False
    if board[y][cursor_x]==0 or board[y][cursor_x]==-1:
      return False
  
def pos5(cursor_x,cursor_y,stone): #左上
  cnt=0
  if cursor_x>cursor_y:
    i_max=cursor_y
  else:
    i_max=cursor_x
  for i in range(i_max-1):
      if board[cursor_y-i][cursor_x-i]==2 if stone==True else 1:
        cnt=cnt+1
      if board[cursor_y-i][cursor_x-i]==1 if stone==True else 2:
        if cnt>0:
          return True
        else:
          return False
      if board[cursor_y-i][cursor_x-i]==0 or board[cursor_y-i][cursor_x-i]==-1:
        return False

def pos6(cursor_x,cursor_y,stone): #右下
  cnt=0
  if 8-cursor_x+1>8-cursor_y+1:
    i_max=8-cursor_y+1
  else:
    i_max=8-cursor_x+1
  for i in range(i_max-1):
      if board[cursor_y+i][cursor_x+i]==2 if stone==True else 1:
        cnt=cnt+1
      if board[cursor_y+i][cursor_x+i]==1 if stone==True else 2:
        if cnt>0:
          return True
        else:
          return False
      if board[cursor_y+i][cursor_x+i]==0 or board[cursor_y+i][cursor_x+i]==-1:
        return False
  
def pos7(cursor_x,cursor_y,stone): #左下
  cnt=0
  if cursor_x>8-cursor_y+1:
    i_max=8-cursor_y+1
  else:
    i_max=cursor_x
  for i in range(i_max-1):
      if board[cursor_y+i][cursor_x-i]==2 if stone==True else 1:
        cnt=cnt+1
      if board[cursor_y+i][cursor_x-i]==1 if stone==True else 2:
        if cnt>0:
          return True
        else:
          return False
      if board[cursor_y+i][cursor_x-i]==0 or board[cursor_y+i][cursor_x-i]==-1:
        return False
  
def pos8(cursor_x,cursor_y,stone): #右上
  cnt=0
  if 8-cursor_x+1>cursor_y:
    i_max=cursor_y
  else:
    i_max=8-cursor_x+1
  for i in range(0,i_max-1):
    if board[cursor_y-i][cursor_x+i]==2 if stone==True else 1:
      cnt=cnt+1
    if board[cursor_y-i][cursor_x+i]==1 if stone==True else 2:
      if cnt>0:
        return True
      else:
        return False
    if board[cursor_y-i][cursor_x+i]==0 or board[cursor_y-i][cursor_x+i]==-1:
      return False
    
      
  
    
  
   
 
      

  




def put_stone():
  global cursor_x,cursor_y
  cursor_x=(mouse_x-185)//54.375+1
  cursor_y=(mouse_y-80)//54.375+1
  if mouse_c==1 and cursor_x>=0 and cursor_x<8 and cursor_y>=0 and cursor_y<8:
    if board[cursor_y][cursor_x]==0:
      if pos1(cursor_x,cursor_y,stone)==True or pos2(cursor_x,cursor_y,stone)==True or pos3(cursor_x,cursor_y,stone)==True or pos4(cursor_x,cursor_y,stone)==True or pos5(cursor_x,cursor_y,stone)==True or pos6(cursor_x,cursor_y,stone)==True or pos7(cursor_x,cursor_y,stone)==True or pos8(cursor_x,cursor_y,stone)==True:
        board[cursor_y][cursor_x]=1 if stone==True else 2
        draw_board()
        sound2()

def chaeck_board(cursor_x,cursor_y,stone):
  for y in range(8):
    for x in range(8):
      check[y][x]=board[y][x]
  if pos1(cursor_x,cursor_y,stone)==True:
    cnt=0   #左
    for x in range(cursor_x-1,0,-1):
      if board[cursor_y][x]==2 if stone==True else 1:
        cnt=cnt+1
      if board[cursor_y][x]==1 if stone==True else 2:
        if cnt>0:
          for i in range(cnt):
            check[cursor_y][cursor_x-i]=1 if stone==True else 2
          break
        else:
          break
      if board[cursor_y][x]==0 or board[cursor_y][x]==-1:
        break
    
  if pos2(cursor_x,cursor_y,stone)==True:
    cnt=0   #右
    for x in range(cursor_x+1,10):
      if board[cursor_y][x]==2 if stone==True else 1:
        cnt=cnt+1
        if board[cursor_y][x]==1 if stone==True else 2:
          if cnt>0:
            for i in range(cnt):
              check[cursor_y][cursor_x+i]=1 if stone==True else 2
            break
          else:
            break
      if board[cursor_y][x]==0 or board[cursor_y][x]==-1:
        break
  
  if pos3(cursor_x,cursor_y,stone)==True:
    cnt=0   #上
    for y in range(cursor_y+1,10):
      if board[y][cursor_x]==2 if stone==True else 1:
        cnt=cnt+1
      if board[y][cursor_x]==1 if stone==True else 2:
        if cnt>0:
          for i in range(cnt):
            check[cursor_y+i][cursor_x]=1 if stone==True else 2
          break
        else:
          break
      if board[y][cursor_x]==0 or board[y][cursor_x]==-1:
        break
  
  if pos4(cursor_x,cursor_y,stone)==True:
    cnt=0   #下
    for y in range(cursor_y-1,0,-1):
      if board[y][cursor_x]==2 if stone==True else 1:
        cnt=cnt+1
      if board[y][cursor_x]==1 if stone==True else 2:
        if cnt>0:
          for i in range(cnt):
            check[cursor_y-i][cursor_x]=1 if stone==True else 2
          break
        else:
          break
      if board[y][cursor_x]==0 or board[y][cursor_x]==-1:
        break
    
  if pos5(cursor_x,cursor_y,stone)==True:
    cnt=0   #左上
    if cursor_x>cursor_y:
      i_max=cursor_y
    else:
      i_max=cursor_x
    for i in range(i_max-1):
      if board[cursor_y-i][cursor_x-i]==2 if stone==True else 1:
        cnt=cnt+1
      if board[cursor_y-i][cursor_x-i]==1 if stone==True else 2:
        if cnt>0:
          for i in range(cnt):
            check[cursor_y-i][cursor_x-i]=1 if stone==True else 2
          break
        else:
          break
      if board[cursor_y-i][cursor_x-i]==0 or board[cursor_y-i][cursor_x-i]==-1:
        break
  
  if pos6(cursor_x,cursor_y,stone)==True:
    cnt=0   #右下
    if 8-cursor_x+1>8-cursor_y+1:
      i_max=8-cursor_y+1
    else:
      i_max=8-cursor_x+1
    for i in range(i_max-1):
      if board[cursor_y+i][cursor_x+i]==2 if stone==True else 1:
        cnt=cnt+1
      if board[cursor_y+i][cursor_x+i]==1 if stone==True else 2:
        if cnt>0:
          for i in range(cnt):
            check[cursor_y+i][cursor_x+i]=1 if stone==True else 2
          break
        else:
          break
      if board[cursor_y+i][cursor_x+i]==0 or board[cursor_y+i][cursor_x+i]==-1:
        break
    
  if pos7(cursor_x,cursor_y,stone)==True:
    cnt=0   #左下
    if cursor_x>8-cursor_y+1:
      i_max=8-cursor_y+1
    else:
      i_max=cursor_x
    for i in range(i_max-1):
      if board[cursor_y+i][cursor_x-i]==2 if stone==True else 1:
        cnt=cnt+1
      if board[cursor_y+i][cursor_x-i]==1 if stone==True else 2:
        if cnt>0:
          for i in range(cnt):
            check[cursor_y+i][cursor_x-i]=1 if stone==True else 2
          break
        else:
          break
      if board[cursor_y+i][cursor_x-i]==0 or board[cursor_y+i][cursor_x-i]==-1:
        break
  
  if pos8(cursor_x,cursor_y,stone)==True:
    cnt=0   #右上
    if 8-cursor_x+1>cursor_y:
      i_max=cursor_y
    else:
      i_max=8-cursor_x+1
    for i in range(0,i_max-1):
      if board[cursor_y-i][cursor_x+i]==2 if stone==True else 1:
        cnt=cnt+1
      if board[cursor_y-i][cursor_x+i]==1 if stone==True else 2:
        if cnt>0:
          for i in range(cnt):
            check[cursor_y-i][cursor_x+i]=1 if stone==True else 2
          break
        else:
          break
      if board[cursor_y-i][cursor_x+i]==0 or board[cursor_y-i][cursor_x+i]==-1:
        break
    

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