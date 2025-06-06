#part 1
with open('input.txt') as file:
    contents=file.readlines()
    a,b=[],[]
    for i in contents:
        a+=[int(i.split()[0])]
        b+=[int(i.split()[1])]
    a.sort()
    b.sort()

    s=sum(map(lambda x,y: abs(x-y),a,b))
print(s)


#part 2
with open('input.txt') as file:
    contents=file.readlines()
    a,b=[],[]
    for i in contents:
        a+=[int(i.split()[0])]
        b+=[int(i.split()[1])]
    a_dict={i: a.count(i) for i in a}
    b_dict={i: b.count(i) for i in b}
    s=0
    for i in a_dict:
        s+=i*a_dict[i]*b_dict.get(i,0)
    print(s)