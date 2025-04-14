with open('input.txt', 'r') as f:
    content=f.readlines()
    M=len(content)
    #haven't gotten rid of the \n yet
    N=len(content[0])-1

    #store coords of antennas in dictionary:
    #info={'0': [(1, 8), (2, 5), (3, 7), (4, 4)], 'A': [(5, 6), (8, 8), (9, 9)]}
    info={}
    for line in range(M):
        line_list=list(content[line].strip('\n'))
        for i in range(N):
            if line_list[i]!='.':
                if line_list[i] in info.keys():
                    info[line_list[i]]+=[(line,i)]
                else:
                    info[line_list[i]]=[(line,i)]

    #function to determine if coords in range
    def safe(x:tuple):
        a,b=x
        if 0<=a<M and 0<=b<N:
            return True
        else:
            return False

    #store coords of antinodes in list of tuples
    antinodes=[]
    for letter in info.keys():
        if len(info[letter])>1:
            for i in range(len(info[letter])):
                for j in range(i+1,len(info[letter])):
                    a = info[letter][i][0] - info[letter][j][0]
                    b = info[letter][i][1] - info[letter][j][1]


                    #part 1
                    #(1, 8) (2, 5) gives (0,11) (3,2)

                    # anti1=(info[letter][i][0]+a,info[letter][i][1]+b)
                    # anti2=(info[letter][j][0]-a,info[letter][j][1]-b)
                    #
                    # #if coords  not duplicate and not out of range
                    # if anti1 not in antinodes and safe(anti1):
                    #     antinodes.append(anti1)
                    # if anti2 not in antinodes and safe(anti2):
                    #     antinodes.append(anti2)


                    # part 2
                    next1 = info[letter][i]
                    next2 = info[letter][j]
                    while safe(next1):
                        if next1 not in antinodes:
                            antinodes.append(next1)
                        next1 = (next1[0] + a, next1[1] + b)

                    while safe(next2):
                        if next2 not in antinodes:
                            antinodes.append(next2)
                        next2 = (next2[0] - a, next2[1] - b)

    print(len(antinodes))


# part 1
# A: 3 antennas (3!=6 antinodes but 1 out of range) 5
# O: 4 antennas (4!=12 antinodes but 2 out of range) 10
# 1 overlap (5+10-1)=14