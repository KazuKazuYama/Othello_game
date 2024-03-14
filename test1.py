cursor_x=4
cursor_y=6
stone=True
board=[[0 for i in range(10)] for j in range(10)]
board[4][4]=1
board[4][5]=2
board[5][4]=2
board[5][5]=1
board[cursor_y][cursor_x]=1
for i in range(10):
  for j in range(10):
    print(board[i][j],end=" ")
  print()

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

def check(cursor_x,cursor_y,stone):
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



print(pos4(cursor_x,cursor_y,stone))
check(cursor_x,cursor_y,stone)
print("変化後")
for i in range(10):
  for j in range(10):
    print(board[i][j],end=" ")
  print()