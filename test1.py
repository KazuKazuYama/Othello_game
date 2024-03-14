cursor_x=6
cursor_y=3
stone=True
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

def pos7(cursor_x,cursor_y,stone): #左下
  cnt=0
  if cursor_x>8-cursor_y+1:
    i_max=8-cursor_y+1
  else:
    i_max=cursor_x
    i_max=3
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

def check(cursor_x,cursor_y,stone):
 if pos7(cursor_x,cursor_y,stone)==True:
    cnt=0   #左下
    if cursor_x>8-cursor_y+1:
      i_max=8-cursor_y+1
    else:
      i_max=cursor_x
    
    i_max=3
    print(i_max)
    for i in range(1,i_max):
      if board[cursor_y+i][cursor_x-i]==2 if stone==True else board[cursor_y+i][cursor_x-i]==1:
        cnt=cnt+1
        print(cnt)
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



print(pos7(cursor_x,cursor_y,stone))
check(cursor_x,cursor_y,stone)
print("変化後")
for i in range(10):
  for j in range(10):
    print(board[i][j],end=" ")
  print()