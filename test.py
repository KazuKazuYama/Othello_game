import random

cursor_x=6
cursor_y=3
stone=False
board=[[0 for i in range(10)] for j in range(10)]
board[4][4]=1
board[4][5]=2
board[5][4]=1
board[5][5]=2
board[cursor_y][cursor_x]=1
for i in range(10):
  for j in range(10):
    print(board[i][j],end=" ")
  print()

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
  for i in range(1,i_max-1):
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
  for i in range(1,i_max-1):
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
  for i in range(1,i_max-1):
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
  for i in range(1,i_max-1):
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

def com_put_stone(): #コンピュータの石を置く
  global c_x,c_y,stone,com_x,com_y
  c_x=[]
  c_y=[]

  for y in range(1,9):
    for x in range(1,9):
      if pos1(x,y,stone)==True or pos2(x,y,stone)==True or pos3(x,y,stone)==True or pos4(x,y,stone)==True or pos5(x,y,stone)==True or pos6(x,y,stone)==True or pos7(x,y,stone)==True or pos8(x,y,stone)==True:
        c_x.append(x)
        c_y.append(y)
       
  print(len(c_x))
  i=random.randint(0,len(c_x)-1)
  com_x=c_x[i]
  com_y=c_y[i]
  if stone==True:
    board[com_y][com_x]=2
  else:
    board[com_y][com_x]=1
      
        
  
  
print(pos7(cursor_x,cursor_y,stone))
com_put_stone()
print(c_x)
print(c_y)
print("変化後")
for i in range(10):
  for j in range(10):
    print(board[i][j],end=" ")
  print()