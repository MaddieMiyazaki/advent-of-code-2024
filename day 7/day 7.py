from copy import deepcopy

with open('input.txt', 'r') as f:
    content = f.readlines()
    count=0
    for line in content:
        sol=int(line.split(': ')[0])
        x=list(map(int,(line.split(': ')[1].strip('\n')).split(' ')))
        def smallerthansol(i):
            return i<=sol
        new = [x[0]]

        #consider each remaining value in that list one at a time
        for i in range(1,len(x)):
            last=deepcopy(new)
            new=[]

            for element in last:
                new.append(element+x[i])
                new.append(element*x[i])

                #added for part 2
                new.append(int(str(element)+str(x[i])))

            #remove any values that are greater than sol as these cannot become solutions
            new=(list(filter(smallerthansol,new)))
        if sol in new:
            count += sol

    print(count)


#8401132154762

#95297119227552



