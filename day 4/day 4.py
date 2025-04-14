import numpy as np
#take in four lines of text to search for the four different arrangements of xmas

def type1(block):
    count=0
    for line in block:
        count+=line.count('SAMX')
        count+=line.count('XMAS')
    return count

#vertical
def type2(block):
    count=0
    x = [list(j.strip('\n')) for j in block]
    y=[''.join(j) for j in np.transpose(x)]
    for line in y:
        count+=line.count('SAMX')
        count+=line.count('XMAS')
    return count

#right diagonal
def type3(block):
    shifted_block=[('.'*(4-i))+block[i].strip('\n')+('.'*i) for i in range(4)]
    return type2(shifted_block)

#left diagonal
def type4(x):
    shifted_block = [('.' * i) + block[i].strip('\n') + ('.' * (4-i)) for i in range(4)]
    return type2(shifted_block)

with open('input.txt','r') as file:
    contents=file.readlines()
    count = 0

    #type 1: horizontal
    count+=type1(contents)

    #diagnonals and verticals
    i=0
    valid=True
    while valid:
        block=contents[i:i+4]
        if len(block)==4:
            count+=type2(block)+type3(block)+type4(block)
            i+=1
        else:
            valid=False
    print(count)

#take a block of three lines, search for 'mas' or 'sam'
#return a list of indices
#check where they align

def search_diag(shifted):
    x = [list(j.strip('\n')) for j in shifted]
    y = [''.join(j) for j in np.transpose(x)]
    indices = [i for i in range(len(y)) if y[i] == 'MAS' or y[i] == 'SAM']
    return indices

#use above function
def cross(block):
    count=0
    right_shifted_block = [('.' * (3 - i)) + block[i].strip('\n') + ('.' * i) for i in range(3)]
    left_shifted_block = [('.' * i) + block[i].strip('\n') + ('.' * (3-i)) for i in range(3)]
    right_indices=search_diag(right_shifted_block)
    left_indices=[i+1 for i in search_diag(left_shifted_block)]
    #check they align
    for i in right_indices:
        if i in left_indices:
            count+=1
    return count


with open('input.txt','r') as file:
    contents=file.readlines()
    count = 0
    i = 0
    valid = True
    while valid:
        block = contents[i:i + 3]
        if len(block) == 3:
            count += cross(block)
            i += 1
        else:
            valid = False
    print(count)