with open('input.txt', 'r') as f:
    content = f.read()
    N=len(content)
    files=[int(content[i]) for i in range(N) if i%2==0]
    gaps=[int(content[i]) for i in range(N) if i%2==1]

    actual=[]
    for i in range(len(content)):
        if i%2==1:
            actual+=['.']*int(content[i])
        else:
            actual+=[int(i/2)]*int(content[i])

    a=len(actual)-1
    reordered=[0]*sum(files)
    for i in range(sum(files)):
        if actual[i]=='.':
            while actual[a]=='.':
                a-=1
            reordered[i]=actual[a]
            a-=1
        else:
            reordered[i]=actual[i]

    count=0
    for i in range(len(reordered)):
        count+=i*reordered[i]
    print(count)



#part 2
    #dictionary of location of all gaps and their lengths
    gap_dict={}
    ind = files[0]
    for i in range(len(gaps)):
        gap_dict[ind]=gaps[i]
        ind+=files[i+1]+gaps[i]

    for i in range(len(files)-1):
        file_id=len(files)-i-1
        size=len(files)-1-i
        a=actual.index(file_id)

        #find next available gap
        for m,n in gap_dict.items():
            if n>=files[size]:
                #move files
                for j in range(m,m+files[size]):
                    actual[j]=file_id
                for j in range(a,a+files[size]):
                    actual[j]='.'

                # update dictionary
                del gap_dict[m]
                if files[size]<n:
                    gap_dict[m+files[size]] = n-files[size]
                gap_dict=dict(sorted(gap_dict.items()))
                break

    count = 0
    for i in range(len(actual)):
        if actual[i]!='.':
            count += i * actual[i]
    print(count)
