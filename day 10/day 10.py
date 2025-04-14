from copy import deepcopy

with open('input.txt','r') as f:
    #list of list of integers
    contents=[list(map(int,list(i.strip('\n'))))for i in f.readlines()]
    M=len(contents)
    N=len(contents[0])
    count=0

    #check coords in range:
    def safe(coord:tuple):
        a,b=coord
        return 0<=a<M and 0<=b<N

    #returns list of tuples for up to 4 legal surrounding coords (ie remove coords out of range using safe)
    def next_in_path(coord: tuple):
        a,b=coord
        return list(filter(safe,[(a+1,b),(a-1,b),(a,b-1),(a,b+1)]))


    #find coords all zeros. store in list
    z=[(m,n) for n in range(N) for m in range(M) if contents[m][n]==0]


    #at each zero, wander until nine reached and note its coord. count every unique path
    for zero in z:

        #list of current coords that the value i is at. ie as we wander, keep track of the end point of every valid path
        #list of tuples
        current_paths=[zero]          #coord of first zero eg [(6,0)]
        for i in range(1,10):

            #function to check if the value at a coord is i
            def valid(i,j:tuple):
                a,b=j
                return contents[a][b]==i

            #keep track of the last coordinate reached for each valid path
            #available is the list of coords of all 'next steps' that allow the path to increase by one
            A=deepcopy(current_paths)
            current_paths=[]
            for coord in A:
                available=list(filter(lambda coord:valid(i,coord),next_in_path(coord)))
                current_paths+=available

            #no more valid routes
            if not current_paths:
                break

        #part 1: set as we only want unique nines
        #count+=len(set(current_paths))

        #part 2: all possible routes
        count+=len(current_paths)

    print('count', count)
