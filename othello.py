import tkinter as tk
import random
import winsound
from PIL import Image, ImageTk

KURO=1
SIRO=2
index=0
pas=0
tmr=0

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
  
def init_false():
  for y in range(10):
    for x in range(10):
      [y][x]=False

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
    if board[cursor_y][x]==2 if stone==True else board[cursor_y][x]==1:
      cnt=cnt+1
    if board[cursor_y][x]==1 if stone==True else board[cursor_y][x]==2:
      if cnt>0:
        return True
      else:
        return False
    if board[cursor_y][x]==0 or board[cursor_y][x]==-1:
      return False
  return False
    
def pos2(cursor_x,cursor_y,stone): #右
  cnt=0
  for x in range(cursor_x+1,10):
    if board[cursor_y][x]==2 if stone==True else board[cursor_y][x]==1:
      cnt=cnt+1
    if board[cursor_y][x]==1 if stone==True else board[cursor_y][x]==2:
        if cnt>0:
            return True
        else:
            return False
    if board[cursor_y][x]==0 or board[cursor_y][x]==-1:
      return False
  return False

def pos3(cursor_x,cursor_y,stone):  #下
  cnt=0
  for y in range(cursor_y+1,10):
    if board[y][cursor_x]==2  if stone==True else board[y][cursor_x]==1:
      cnt=cnt+1
    if board[y][cursor_x]==1 if stone==True else board[y][cursor_x]==2:
      if cnt>0:
        return True
      else:
        return False
    if board[y][cursor_x]==0 or board[y][cursor_x]==-1:
      return False
  return False

def pos4(cursor_x,cursor_y,stone):
  
  cnt=0
  for y in range(cursor_y-1,0,-1): #上
    if board[y][cursor_x]==2 if stone==True else board[y][cursor_x]==1:
      cnt=cnt+1
    if board[y][cursor_x]==1 if stone==True else board[y][cursor_x]==2:
      if cnt>0:
        return True
      else:
        return False
    if board[y][cursor_x]==0 or board[y][cursor_x]==-1:
      return False
  return False
  
def pos5(cursor_x,cursor_y,stone): #左上
  cnt=0
  if cursor_x>cursor_y:
    i_max=cursor_y
  else:
    i_max=cursor_x
  for i in range(1,i_max):
      if board[cursor_y-i][cursor_x-i]==2 if stone==True else board[cursor_y-i][cursor_x-i]==1:
        cnt=cnt+1
      if board[cursor_y-i][cursor_x-i]==1 if stone==True else  board[cursor_y-i][cursor_x-i]==2:
        if cnt>0:
          return True
        else:
          return False
      if board[cursor_y-i][cursor_x-i]==0 or board[cursor_y-i][cursor_x-i]==-1:
        return False
  return False

def pos6(cursor_x,cursor_y,stone): #右下
  cnt=0
  if 8-cursor_x+1>8-cursor_y+1:
    i_max=8-cursor_y+1
  else:
    i_max=8-cursor_x+1
  for i in range(1,i_max):
      if board[cursor_y+i][cursor_x+i]==2 if stone==True else board[cursor_y+i][cursor_x+i]==1:
        cnt=cnt+1
      if board[cursor_y+i][cursor_x+i]==1 if stone==True else board[cursor_y+i][cursor_x+i]==2:
        if cnt>0:
          return True
        else:
          return False
      if board[cursor_y+i][cursor_x+i]==0 or board[cursor_y+i][cursor_x+i]==-1:
        return False
  return False
  
def pos7(cursor_x,cursor_y,stone): #左下
  cnt=0
  if cursor_x>8-cursor_y+1:
    i_max=8-cursor_y+1
  else:
    i_max=cursor_x
  for i in range(1,i_max):
      if board[cursor_y+i][cursor_x-i]==2 if stone==True else board[cursor_y+i][cursor_x-i]==1:
        cnt=cnt+1
      if board[cursor_y+i][cursor_x-i]==1 if stone==True else board[cursor_y+i][cursor_x-i]==2:
        if cnt>0:
          return True
        else:
          return False
      if board[cursor_y+i][cursor_x-i]==0 or board[cursor_y+i][cursor_x-i]==-1:
        return False
  return False
  
def pos8(cursor_x,cursor_y,stone): #右上
  cnt=0
  if 8-cursor_x+1>cursor_y:
    i_max=cursor_y
  else:
    i_max=8-cursor_x+1
  for i in range(1,i_max):
    if board[cursor_y-i][cursor_x+i]==2 if stone==True else board[cursor_y-i][cursor_x+i]==1:
      cnt=cnt+1
    if board[cursor_y-i][cursor_x+i]==1 if stone==True else board[cursor_y-i][cursor_x+i]==2:
      if cnt>0:
        return True
      else:
        return False
    if board[cursor_y-i][cursor_x+i]==0 or board[cursor_y-i][cursor_x+i]==-1:
      return False
  return False
    
def all_confirm(stone): #置ける場所があるかどうか
  for y in range(1,9):
    for x in range(1,9):
      if board[y][x]==0:
        if pos1(x,y,stone)==True or pos2(x,y,stone)==True or pos3(x,y,stone)==True or pos4(x,y,stone)==True or pos5(x,y,stone)==True or pos6(x,y,stone)==True or pos7(x,y,stone)==True or pos8(x,y,stone)==True:
         return True
  return False #置ける場所がない

def my_put_stone(): #自分の石を置く
  global cursor_x,cursor_y,stone,mouse_c
    
  if board[cursor_y][cursor_x]==0:
    if pos1(cursor_x,cursor_y,stone)==True or pos2(cursor_x,cursor_y,stone)==True or pos3(cursor_x,cursor_y,stone)==True or pos4(cursor_x,cursor_y,stone)==True or pos5(cursor_x,cursor_y,stone)==True or pos6(cursor_x,cursor_y,stone)==True or pos7(cursor_x,cursor_y,stone)==True or pos8(cursor_x,cursor_y,stone)==True:
      if stone==True:
        board[cursor_y][cursor_x]=1
      else:
        board[cursor_y][cursor_x]=2
      draw_board()
      sound2()
      
    else:# 空白に置けない場合
      return False
  #pos,checkのところでおいている石も 
    

def com_put_stone(): #コンピュータの石を置く
  global c_x,c_y,stone,com_x,com_y
  c_x=[]
  c_y=[]

  for y in range(1,9):
    for x in range(1,9):
      if pos1(x,y,stone)==True or pos2(x,y,stone)==True or pos3(x,y,stone)==True or pos4(x,y,stone)==True or pos5(x,y,stone)==True or pos6(x,y,stone)==True or pos7(x,y,stone)==True or pos8(x,y,stone)==True:
        if board[y][x]==0:
          c_x.append(x)
          c_y.append(y)
      
  i=random.randint(0,len(c_x)-1)
  com_x=c_x[i]
  com_y=c_y[i]
  if stone==True:
    board[com_y][com_x]=1
  else:
    board[com_y][com_x]=2
  check_board(com_x,com_y,stone)
  draw_board()
  sound2()
    
def check_board(cursor_x,cursor_y,stone):#石を置いたときの処理
  if pos1(cursor_x,cursor_y,stone)==True:
    cnt=0   #左
    for x in range(cursor_x-1,0,-1):
      if board[cursor_y][x]==2 if stone==True else board[cursor_y][x]==1:
        cnt=cnt+1
      if board[cursor_y][x]==1 if stone==True else board[cursor_y][x]==2:
        if cnt>0:
          for i in range(cnt):
            if stone==True:
              board[cursor_y][cursor_x-i-1]=1
            else:
              board[cursor_y][cursor_x-i-1]=2
          break
        else:
          break
      if board[cursor_y][x]==0 or board[cursor_y][x]==-1:
        break
 
  if pos2(cursor_x,cursor_y,stone)==True:
    cnt=0   #右
    for x in range(cursor_x+1,10):
      if board[cursor_y][x]==2 if stone==True else board[cursor_y][x]==1:
        cnt=cnt+1
      if board[cursor_y][x]==1 if stone==True else board[cursor_y][x]==2:
        if cnt>0:
          for i in range(cnt):
            if stone==True:
              board[cursor_y][cursor_x+i+1]=1
            else:
              board[cursor_y][cursor_x+i+1]=2
          break
        else:
          break
      if board[cursor_y][x]==0 or board[cursor_y][x]==-1:
        break
  
  if pos3(cursor_x,cursor_y,stone)==True:
    cnt=0   #下
    for y in range(cursor_y+1,10):
      if board[y][cursor_x]==2 if stone==True else board[y][cursor_x]==1:
        cnt=cnt+1
      if board[y][cursor_x]==1 if stone==True else board[y][cursor_x]==2:
        if cnt>0:
          for i in range(cnt):
            if stone==True:
              board[cursor_y+i+1][cursor_x]=1
            else:
              board[cursor_y+i+1][cursor_x]=2
            
          break
        else:
          break
      if board[y][cursor_x]==0 or board[y][cursor_x]==-1:
        break
  
  if pos4(cursor_x,cursor_y,stone)==True:
    cnt=0   #上
    for y in range(cursor_y-1,0,-1):
      if board[y][cursor_x]==2 if stone==True else board[y][cursor_x]==1:
        cnt=cnt+1
      if board[y][cursor_x]==1 if stone==True else board[y][cursor_x]==2:
        if cnt>0:
          for i in range(cnt):
            if stone==True:
              board[cursor_y-i-1][cursor_x]=1
            else:
              board[cursor_y-i-1][cursor_x]=2
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
    for i in range(1,i_max):
      if board[cursor_y-i][cursor_x-i]==2 if stone==True else board[cursor_y-i][cursor_x-i]==1:
        cnt=cnt+1
      if board[cursor_y-i][cursor_x-i]==1 if stone==True else board[cursor_y-i][cursor_x-i]==2:
        if cnt>0:
          for i in range(cnt):
            if stone==True:
              board[cursor_y-i-1][cursor_x-i-1]=1
            else:
              board[cursor_y-i-1][cursor_x-i-1]=2
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
    for i in range(1,i_max):
      if board[cursor_y+i][cursor_x+i]==2 if stone==True else board[cursor_y+i][cursor_x+i]==1:
        cnt=cnt+1
      if board[cursor_y+i][cursor_x+i]==1 if stone==True else board[cursor_y+i][cursor_x+i]==2:
        if cnt>0:
          for i in range(cnt):
            if stone==True:
              board[cursor_y+i+1][cursor_x+i+1]=1
            else:
              board[cursor_y+i+1][cursor_x+i+1]=2
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
    for i in range(1,i_max):
      if board[cursor_y+i][cursor_x-i]==2 if stone==True else board[cursor_y+i][cursor_x-i]==1:
        cnt=cnt+1
      if board[cursor_y+i][cursor_x-i]==1 if stone==True else board[cursor_y+i][cursor_x-i]==2:
        if cnt>0:
          for i in range(cnt):
            if stone==True:
              board[cursor_y+i+1][cursor_x-i-1]=1
            else:
              board[cursor_y+i+1][cursor_x-i-1]=2
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
    for i in range(1,i_max):
      if board[cursor_y-i][cursor_x+i]==2 if stone==True else board[cursor_y-i][cursor_x+i]==1:
        cnt=cnt+1
      if board[cursor_y-i][cursor_x+i]==1 if stone==True else board[cursor_y-i][cursor_x+i]==2:
        if cnt>0:
          for i in range(cnt):
            if stone==True:
              board[cursor_y-i-1][cursor_x+i+1]=1
            else:
              board[cursor_y-i-1][cursor_x+i+1]=2
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
  winsound.Beep(392,300)
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

def sound4(): #引き分け時の音
  winsound.Beep(392,300)
  winsound.Beep(392,300)
  winsound.Beep(392,300)
  winsound.Beep(310,1000)
  winsound.Beep(349,300)
  winsound.Beep(349,300)
  winsound.Beep(349,300)
  winsound.Beep(293,1000)
  
def sound5(): #石を置けないときの音
  winsound.Beep(261,100) 

def main_game():
  global index,stone,tmr,ban,pas,tmr
  global cursor_x,cursor_y,mouse_x,mouse_y,mouse_c
  
  if index==0:
    cvs.create_image(400,300,image=bg,tags="TITLE")
    cvs.create_text(400,250,text="オセロ対戦",fill="Black",font=("Times New Roman",70),tag="TITLE")
    cvs.create_text(400,400,text="対局する",fill="Black",font=("Times New Roman",40),tag="TITLE")
    if mouse_c==1 and 280<mouse_x and mouse_x<500 and 370<mouse_y and mouse_y<430:
      sound2()
      mouse_c=0
      index=1
      
  
  elif index==1:
    cvs.delete("TITLE")
    cvs.create_image(400,300,image=bg,tags="SELECT")
    cvs.create_text(250,300,text="先行(黒)",fill="Black",font=("Times New Roman",40),tag="SELECT")
    cvs.create_text(550,300,text="後攻(白)",fill="Black",font=("Times New Roman",40),tag="SELECT")
    if mouse_c==1 and 150<mouse_x and mouse_x<350 and 250<mouse_y and mouse_y<350:
      mouse_c=0
      sound2()
      index=2
      ban=0
       #先攻
    if mouse_c==1 and 450<mouse_x and mouse_x<650 and 250<mouse_y and mouse_y<350:
      mouse_c=0
      sound2()
      index=2
      ban=1
       #後攻
      
    
  elif index==2:
    cvs.delete("SELECT")
    cvs.create_image(400,300,image=bg,tags="BG")
    init_board()
    draw_board()
    if ban==0:
      index=3
     
    if ban==1:
      index=5
    
    
  elif index==3: #先行の時の自分のターン
    stone=True
    cvs.delete("TURN")
    cvs.create_text(720,160,text="あなた",fill="Black",font=("Times New Roman",30),tag="TURN")
    cvs.create_text(720,230,text="黒",fill="Black",font=("Times New Roman",20),tag="TURN")
    if all_confirm(stone)==False:
        pas=pas+1
        sound5()
        index=4
        tmr=0
       
    if all_confirm(stone)==True:
      if mouse_x>185 and mouse_x<615 and mouse_y>80 and mouse_y<530:
        cursor_x=int((mouse_x-185)/54.375)+1
        cursor_y=int((mouse_y-80)/54.375)+1
        pas=0
      
        if mouse_c==1 and board[cursor_y][cursor_x]==0:
          mouse_c=0
          my_put_stone()
          if my_put_stone()==False:
            index=3
          else:
            check_board(cursor_x,cursor_y,stone)
            draw_board()
            index=4
            tmr=0
    if pas==2:
       index=7
            
        
  elif index==4: #先行の時のコンピュータのターン
    stone=False
    tmr=tmr+1
    cvs.delete("TURN")
    cvs.create_text(720,160,text="CP",fill="Black",font=("Times New Roman",30),tag="TURN")
    if tmr==10:
      if all_confirm(stone)==False:
          cvs.delete("TURN")
          cvs.create_text(720,160,text="パス",fill="Black",font=("Times New Roman",30),tag="TURN")
          pas=pas+1
          sound5()
          index=3
      
      if all_confirm(stone)==True:
        com_put_stone()
        check_board(com_x,com_y,stone)
        draw_board()
        pas=0
        index=3
      if pas==2:
        index=7
  
  elif index==5: #後攻の時のコンピュータのターン
    stone=True
    tmr=tmr+1
    cvs.delete("TURN")
    cvs.create_text(720,160,text="CP",fill="Black",font=("Times New Roman",30),tag="TURN")
    if tmr==10:
      if all_confirm(stone)==False:
            cvs.delete("TURN")
            cvs.create_text(720,160,text="パス",fill="Black",font=("Times New Roman",30),tag="TURN")
            pas=pas+1
            sound5()
            index=6
      
      if all_confirm(stone)==True:
        com_put_stone()
        check_board(com_x,com_y,stone)
        draw_board()
        pas=0
        index=6
      if pas==2:
        index=7
    
  elif index==6: #後攻の時の自分のターン
    stone=False
    cvs.delete("TURN")
    cvs.create_text(720,160,text="あなた",fill="Black",font=("Times New Roman",30),tag="TURN")
    cvs.create_text(720,230,text="白",fill="Black",font=("Times New Roman",20),tag="TURN")
    if all_confirm(stone)==False:
        pas=pas+1
        sound5()
        index=5
        tmr=0
      
    if all_confirm(stone)==True:
      if mouse_x>185 and mouse_x<615 and mouse_y>80 and mouse_y<530:
        cursor_x=int((mouse_x-185)/54.375)+1
        cursor_y=int((mouse_y-80)/54.375)+1
        pas=0
        
        if mouse_c==1 and board[cursor_y][cursor_x]==0:
          mouse_c=0
          my_put_stone()
          if my_put_stone()==False:
            index=6
          else:
            check_board(cursor_x,cursor_y,stone)
            draw_board()
            index=5
            tmr=0
          
    if pas==2:
      index=7
            
  elif index==7: #結果の表示
    black_num=0
    white_num=0
    for y in range(1,9):
      for x in range(1,9):
        if board[y][x]==1:
          black_num=black_num+1
        if board[y][x]==2:
          white_num=white_num+1
    cvs.delete("STONE")
    cvs.delete("BG")
    cvs.delete("TURN")
    cvs.create_text(400,500,text="もう一度対局する",fill="Black",font=("Times New Roman",30),tag="RESULT")
    cvs.create_text(300,300,text="黒:"+str(black_num),fill="Black",font=("Times New Roman",40),tag="RESULT")
    cvs.create_text(500,300,text="白:"+str(white_num),fill="Black",font=("Times New Roman",40),tag="RESULT")
    if black_num>white_num:
      if ban==0:
        cvs.create_image(400,120,image=happy,tag="RESULT")
        cvs.create_text(400,100,text="あなたの勝ちです",fill="Red",font=("Times New Roman",40),tag="RESULT")
        sound3_happy()
      if ban==1:
        cvs.create_text(400,100,text="あなたの負けです",fill="Blue",font=("Times New Roman",40),tag="RESULT")
        sound3_destiny()   
    if black_num<white_num:
      if ban==0:
        cvs.create_text(400,100,text="あなたの負けです",fill="Blue",font=("Times New Roman",40),tag="RESULT")
        sound3_destiny()
      if ban==1:
        cvs.create_image(400,100,image=happy,tag="RESULT")
        cvs.create_text(400,100,text="あなたの勝ちです",fill="Red",font=("Times New Roman",40),tag="RESULT")
        sound3_happy() 
    if black_num==white_num:
      cvs.create_text(400,100,text="引き分けです",fill="Black",font=("Times New Roman",40),tag="RESULT")
      sound3_destiny()    
    if mouse_c==1 and 250<mouse_x and mouse_x<450 and 450<mouse_y and mouse_y<550:
      sound2()
      mouse_c=0
      index=0
      pas=0
      tmr=0
      cvs.delete("RESULT")
         
          
          
  root.after(100,main_game)

root=tk.Tk()
root.title("オセロ対戦")
root.resizable(False,False)
root.bind("<Motion>",mouse_move)
root.bind("<ButtonPress>",mouse_press)
bg=tk.PhotoImage(file="board.png")
happy=tk.PhotoImage(file="smiling-cat.png").subsample(3)
cvs=tk.Canvas(width=800,height=600,background="lightgreen")
cvs.pack()

main_game()
root.mainloop()