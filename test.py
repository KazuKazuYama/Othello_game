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

board = [[0 for i in range(8)] for j in range(8)]
board[4][4]=1
board[3][3]=1
board[3][4]=2
board[4][3]=2
stone=True
for y in range(8):
    for x in range(8):
        print(pos1(x,y,stone),end="")
    print()