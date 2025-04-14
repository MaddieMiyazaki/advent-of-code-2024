# with open('input.txt') as file:
#     contents=file.readlines()
#     count=0
#     for i in contents:
#         list_form=list(map(int, i.split()))
#         diff=list_form[1]-list_form[0]
#         #print(diff)
#         if diff not in [1,2,3,-1,-2,-3]:
#             continue
#         else:
#             for j in range(1,len(list_form)-1):
#                 next_diff=list_form[j+1]-list_form[j]
#                 #print(next_diff)
#                 #print('check change:', next_diff in [1,2,3,-1,-2,-3] and next_diff*diff>0)
#                 if next_diff in [1,2,3,-1,-2,-3] and next_diff*diff>0:
#                     #print('made it past checkpoint')
#                     pass
#                     if j==len(list_form)-2:
#                         count+=1
#                         #print('made it to end of line')
#                 else:
#                     break
#                 diff=next_diff
#         #print('next line')
#     print(count)


#takes in list of differences. If all same sign and in 1,2,3 then return true
def check_list(x:list):
    valid=True
    diff=x[0]
    for i in range(len(x)):
        if diff*x[i]>0 and x[i] in [1,2,3,-1,-2,-3]:
            diff=x[i]
        else:
            valid=False
            break

    return valid

#part 1
with open('input.txt') as file:
    contents=file.readlines()
    count=0
    for i in contents:
        a=[]
        list_form=list(map(int, i.split()))
        for j in range(len(list_form)-1):
            a+=[list_form[j+1]-list_form[j]]
        if check_list(a):
            count+=1
    print(count)


#part 2
with open('input.txt') as file:
    contents=file.readlines()
    count=0
    for i in contents:
        a=[]
        list_form=list(map(int, i.split()))
        for j in range(len(list_form)-1):
            a+=[list_form[j+1]-list_form[j]]
        if check_list(a):
            count+=1
        else:
            for k in range(len(list_form)):
                b=[]
                new_list=list_form[0:k]+list_form[k+1:]
                for j in range(len(new_list) - 1):
                    b += [new_list[j + 1] - new_list[j]]
                if check_list(b):
                    count+=1
                    break

    print(count)

