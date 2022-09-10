import re

f = open('input.txt', 'r')
inp = f.read()
inp = inp.splitlines()

inp_count = int(inp[0])
regex_list = []

for i in range(1, inp_count+1):
    regex_list.append(inp[i])

count2 = int(inp[inp_count+1])
str_list = []

for j in range(inp_count+2,len(inp)):
    str_list.append(inp[j])

for i in range(len(str_list)):
    for j in range(len(regex_list)):
        state = re.match(regex_list[j], str_list[i])
        if state != None:
            print('YES,', str(j + 1))
            break
        elif j == len(regex_list) - 1 and state == None:
            print('NO, 0')
            break
