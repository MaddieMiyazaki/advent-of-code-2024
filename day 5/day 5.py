with open('input.txt','r') as file:
    contents=file.readlines()

    #split the file into its two parts
    a,b=contents[0:contents.index('\n')],contents[contents.index('\n')+1:]
    rules={}
    count=0

    #store rules in a dictionary. keys are the 'befores', values are a list of all 'afters'
    for rule in a:
        before,after=rule.strip('\n').split('|')
        if before not in rules.keys():
            rules[before]=[after]
        else:
            rules[before].append(after)

    #work through each line work through every combination of comparisons that need to be performed
    #an 'illegal' ordering of pairs gets tagged
    #once all pairs in a line have been checked and all ordering is 'legal', add middle value to 'count'
    for line in b:
        line_split=line.strip('\n').split(',')
        valid=True
        for i in range(0,len(line_split)-1):
            for j in range(i+1,len(line_split)):
                if str(line_split[i]) in rules.get(str(line_split[j]),[]):
                    valid=False
            #         break
            # else:
            #     continue
            # break
        #lines commented out aren't strictly necessary but reduce unnecessary computations
        #add middle value for 'legal' lines only
        if valid:
            count+=int(line_split[int((len(line_split)-1)/2)])
    print(count)



    #part 2
    count=0
    for line in b:
        line_split=line.strip('\n').split(',')
        valid=True
        for i in range(0,len(line_split)-1):
            for j in range(i+1,len(line_split)):
                if str(line_split[i]) in rules.get(str(line_split[j]),[]):
                    #swap for every wrong pair
                    temp=line_split[i]
                    line_split[i]=line_split[j]
                    line_split[j]=temp
                    #tag the 'illegal' lines
                    valid=False

        #add middle value for 'illegal' lines only
        if not valid:
            count+=int(line_split[int((len(line_split)-1)/2)])
    print(count)


