#change orientation [0,1,2,3] correspond to [up,right,down,left]
def turn(orientation):
    return (orientation+1)%4

def forward(content,orientation,x,y):
    if orientation == 0:
        x-=1
    if orientation == 1:
        y+=1
    if orientation == 2:
        x+=1
    if orientation == 3:
        y-=1
    return x,y


with open('input.txt','r') as f:
    content=[list(i.strip('\n')) for i in f.readlines()]
    M=len(content)
    N=len(content[0])
    orientation=0
    #for q2
    path=set()

    #coords of guard in x,y
    for i in range(M):
        for j in range(N):
            if content[i][j]=='^':
                x,y=i,j
    content[x][y]='X'

    # x can't be 0 or M, y can't be 0 or N
    valid=True
    while valid:
        no_obstacle=True
        while no_obstacle:
            a,b=x,y
            x,y=forward(content,orientation,x,y)

            if content[x][y]=='#':
                x,y=a,b
                orientation = turn(orientation)
                no_obstacle=False
            else:
                content[x][y]='X'
                path.add((x,y))

            if x in [0,M-1] or y in [0,N-1]:
                valid=False
                no_obstacle=False
    count=0
    for i in content:
        count+=i.count('X')
    print(count)


#path ={(5, 4), (4, 4), (3, 4), (2, 4), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (6, 7), (6, 6), (6, 5), (6, 4), (6, 3), (6, 2), (5, 2), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (8, 7), (9, 7)}

#part 2
from copy import deepcopy

def check(content,x,y,M,N):
    #take in edited list of list then let the guard walk
    #at every step, check he hasn't visited before
    #if loop return False, if able to exit return True
    loop_or_not=True
    orientation=0
    visited=[]
    valid = True
    while valid:
        no_obstacle = True
        while no_obstacle:
            a, b = x, y
            x, y = forward(content, orientation, x, y)

            if content[x][y] == '#':
                x, y = a, b
                orientation = turn(orientation)
                no_obstacle = False
            else:
                if (x,y,orientation) in visited: #then we're stuck in a loop
                    loop_or_not=False
                    valid = False
                    no_obstacle = False
                else: #keep appending to visited
                    visited.append((x,y,orientation))

            if x in [0, M - 1] or y in [0, N - 1]:
                valid = False
                no_obstacle = False

    return loop_or_not


with open('input.txt','r') as f:
    original=[list(i.strip('\n')) for i in f.readlines()]

    count=0
    M = len(original)
    N = len(original[0])

    # coords of guard in x,y
    for i in range(M):
        for j in range(N):
            if original[i][j] == '^':
                x, y = i, j


    for i,j in path:
        content=deepcopy(original)
        content[i][j]='#'
        # for k in content:
        #     print(k)
        #
        # print(check(content,x,y,M,N))
        if not check(content,x,y,M,N):
            count+=1
    print(count)



