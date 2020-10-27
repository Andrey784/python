import pygame
from random import randint as random
pygame.init()
size = 200
r = int(size//2.5
ots = 10
RES = 3*size +  2 * ots, 3*size +  2 * ots
sc = pygame.display.set_mode((RES))
clock = pygame.time.Clock()
x = 0
y = 0
red = (255,0,0)
blue = (0,0,255)
white = (255,255,255)
green = (0,255,0)
mas = [[1,2,3],[4,5,6],[7,8,9]]
count = 0
board = mas[0]+mas[1]+mas[2]
tk = 20
def draw():
    global size,ots,x_col,y_row,mas,red,blue,count,r,tk
    for row in range(3):
        for col in range(3):
            if mas[col][row] == 'x'
                x = size*row + row * ots
                y = size*col + col * ots
                xx = size//10
                yy = size//10
                pygame.draw.line(sc,red,(x+ots+xx,y+yy),(x+size-ots-xx,y+size-yy),tk)
                pygame.draw.line(sc,red,(x+size-ots-xx,y+yy),(x+ots+xx,y+size-yy),tk)
            if mas[col][row] == 'o':
                x = size*row + row * ots
                y = size*col + col * ots
                pygame.draw.circle(sc, blue,(x+(size//2),y+(size//2)),r,tk*2//3)

def win():
    global mas,board
    win = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]
    board = mas[0]+mas[1]+mas[2]
    for i in win:
        if board[i[0]-1]== board[i[1]-1] == board[i[2]-1]:
            return [board[i[0]-1], i]
    return False

def line(i):
    global size,board,tk
    dx = -size//3
    dy = size//3
    xy1 = ((i[0]-1)%3,(i[0]-1)//3)
    xy2 = ((i[2]-1)%3,(i[2]-1)//3) 
    if xy1[1] ==  xy2[1]:
        dx = size//2
        dy = 0
    if xy1[0] ==  xy2[0]:
        dy = size//2
        dx = 0
    if xy1[0] == 0 and xy1[1] == 0 and xy2[0] == 2 and xy2[1] == 2:
        dx = dx*(-1)
    x1 = xy1[0] * size + size//2 + ots - dx
    y1 = xy1[1] * size + size//2 + ots - dy
    x2 = xy2[0] * size + size//2 + ots + dx
    y2 = xy2[1] * size + size//2 + ots + dy
    pygame.draw.line(sc,green,(x1,y1),(x2,y2),tk)
    
def hard():
    global count, mas, board
    win= [(1,2,3),(1,4,7),(1,5,9),(2,5,8),(3,6,9),(3,5,7),(4,5,6),(7,8,9)]
    board = mas[0]+mas[1]+mas[2]
    cw = []
    for i in win:
        c = 0
        l1 = False
        l2 = False
        l3 = False
        if board[i[0]-1]==board[i[1]-1] and board[i[0]-1]=='o':
            c = c + 1
            l1 = True
        if board[i[1]-1]==board[i[2]-1] and board[i[1]-1]=='o':
            c = c + 1
            l2 = True
        if board[i[0]-1]==board[i[2]-1] and board[i[0]-1]=='o':
            c = c + 1
            l3 = True
        if c==1:
            if l1==True:
                if str(board[i[2]-1]) not in 'xo':
                    board[i[2]-1]='o'
                    print('win')
                    return board
            elif l2==True:
                if str(board[i[0]-1]) not in 'xo':
                    board[i[0]-1]='o'
                    print('win')
                    return board
            elif l3==True:
                if str(board[i[1]-1]) not in 'xo':
                   board[i[1]-1]='o'
                   print('win')
                   return board
    
    loose =  [(1,2,3),(1,4,7),(1,5,9),(2,5,8),(3,6,9),(3,5,7),(4,5,6),(7,8,9)]
    for i in loose:
        c = 0
        l1 = False
        l2 = False
        l3 = False
        if board[i[0]-1]==board[i[1]-1] and board[i[0]-1]=='x':
            c = c + 1
            l1 = True
        if board[i[1]-1]==board[i[2]-1] and board[i[1]-1]=='x':
            c = c + 1
            l2 = True
        if board[i[0]-1]==board[i[2]-1] and board[i[0]-1]=='x':
            c = c + 1
            l3 = True
        if c==1:
            if l1==True:
                if str(board[i[2]-1]) not in 'xo':
                    board[i[2]-1]='o'
                    print('loose')
                    return board
            elif l2==True:
                if str(board[i[0]-1]) not in 'xo':
                    board[i[0]-1]='o'
                    print('loose')
                    return board
            elif l3==True:
                if str(board[i[1]-1]) not in 'xo':
                   board[i[1]-1]='o'
                   print('loose')
                   return board
    q = True
    
    
    while q:
        a = 5
        if str(board[a-1]) not in 'xo':
                board[a-1]='o'
                print('центр')
                return board
        a = random(1,9)
        if count == 1 and 'x' == board[4]:
            if str(board[a-1]) not in 'xo' and a not in (2,4,6,8):
                board[a-1]='o'
                print('ситуация 0')
                return board
            else:
                continue
        if count == 3:
            if board[4] == 'o' and 'x' in (board[0],board[2],board[6],board[8]):
                if (board[0] == board[8] and board[0] == 'x') or (board[2] == board[6] and board[2] == 'x'):
                    if str(board[a-1]) not in 'xo' and a not in (1,3,7,9):
                        board[a-1]='o'
                        print('ситуация 1')
                        return board
                    else:
                        continue
                elif board[4] == 'o' and (board[0] == board[5] or board[0] == board[7] or board[0] == board[5] or board[2] == board[3] or board[2] == board[7] or board[6] == board[5] or board[6] == board[1]or board[8] == board[1]or board[8] == board[3]):
                    p = (-1,0)
                    if board[0] == board[5] and board[0]=='x':
                        p = (1,2,4,5,6,7,8,9)
                    if board[0] == board[7] and board[0]=='x':
                        p = (1,2,3,4,5,6,8,9)
                    if board[2] == board[3] and board[2]=='x':
                        p = (2,3,4,5,6,7,8,9)
                    if board[2] == board[7] and board[2]=='x':
                        p = (1,2,3,4,5,6,7,8)
                    if board[6] == board[5] and board[6]=='x':
                        p = (1,2,3,4,5,6,7,8)
                    if board[6] == board[1] and board[1]=='x':
                        p = (2,3,4,5,6,7,8,9)
                    if board[8] == board[1] and board[8]=='x':
                        p = (1,2,4,5,6,7,8,9)
                    if board[8] == board[3] and board[3]=='x':
                        p = (1,2,3,4,5,6,8,9)
                    if str(board[a-1]) not in 'xo' and a not in p:
                        board[a-1]='o'
                        print('ситуация 2')
                        return board
                    else:
                        continue
            elif  board[4] == 'x' and 'x' in (board[0], board[2],board[6],board[8]):
                if str(board[a-1]) not in 'xo' and a not in (2,4,6,8):
                    board[a-1]='o'
                    print('ситуация 3')
                    return board
                else:
                    continue
            elif board[4] == 'o' and 'x' not in (str(board[0]),str(board[2]),str(board[6]),str(board[8])):
                p = (-1,0)
                if str(board[3])=='x' and str(board[7])== 'x':
                    p = (1,2,3,4,5,6,8,9)
                if str(board[7])=='x' and str(board[5])== 'x':
                    p = (1,2,3,4,5,6,7,8)
                if str(board[5])=='x' and str(board[1])== 'x':
                    p = (1,2,4,5,6,7,8,9)
                if str(board[1])=='x' and str(board[3])== 'x':
                    p = (2,3,4,5,6,7,8,9)
                if str(board[a-1]) not in 'xo' and a not in p:
                    board[a-1]='o'
                    print('ситуация 4')
                    return board
                else:
                    continue
        if  str(board[a-1]) not in 'xo':
            print('рандом')
            board[a-1]='o'
            return board
        continue
q = True
def main():
    global count, mas, player,x,y,q
    while True:
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            mas = [[1,2,3],[4,5,6],[7,8,9]]
            x,y = 0,0
            player = 0
            q = True
        board = mas[0]+mas[1]+mas[2]
        count = 0
        for i in board:
            if str(i) == 'x' or str(i) =='o':
                count+=1
        if count == 9:
            mas = [[1,2,3],[4,5,6],[7,8,9]]
            x,y = 0,0
            player = 0
            continue
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif i.type == pygame.MOUSEBUTTONDOWN:
                x_m,y_m = pygame.mouse.get_pos()
                x_col = x_m//(size + ots//2)
                y_row = y_m//(size + ots//2)
                key = pygame.key.get_pressed()
                if str(mas[y_row][x_col]) not in 'xo' and q:
                        mas[y_row][x_col] = 'x'
        sc.fill((0,0,0))
        for row in range(3):
            for col in range(3):
                color = white
                x = size*row + row * ots
                y = size*col + col * ots
                pygame.draw.rect(sc,color,(x,y,size,size))
        if count%2!=0 and q:
            b = hard()
            mas = []
            s = []
            for i in b:
                s.append(i)
                if len(s)==3:
                    mas.append(s)
                    s=[]
        draw()
        if win():
            line(win()[1])
            q = False
        pygame.display.update()
        clock.tick(30)
main()

