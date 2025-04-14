import re
with open('input.txt','r') as f:
    content=f.read()
    s=0
    matches=re.findall(r'mul\(\d+,\d+\)',content)
    for i in matches:
        a,b=i[4:-1].split(',')
        s+=int(a)*int(b)
    print(s)

#mul   finds the string 'mul'
#\d+    finds all positive integers of any number of digits
#\(     brackets need backslash as they are special characters


with open('input.txt','r') as f:
    content=f.read().split('do()')
    s=0
    for i in content:
        segment=i.split('don\'t()')
        matches=re.findall(r'mul\(\d+,\d+\)',segment[0])
        for j in matches:
            a,b=j[4:-1].split(',')
            s += int(a) * int(b)
    print(s)


