s = input("Enter the word\n")
l = []
for i in s:
    l.append(i)
print(l)
def find_index(val):
    rem = val % 26
    ind =  26 - rem
    print(rem,ind)
    return(ind)
def find_index2(val):
    rem = val % 26
    return(rem)
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
condition = input("enter 'l' for left shift or 'r' right shift\n")
n = int(input("enter the number of places to be shifted\n"))
index= []
for i in l:
    index.append(alpha.index(i))
answer = []
result = []
if condition == "l":
    for i in index:
        val = (i-n)
        if val < 0 :
            answer.append(find_index(val))
        else:
            answer.append(val)    
    for i in answer:
         result.append(alpha[i]) 
elif condition == "r":
    for i in index:
        val = (i+n)
        if val > 25 :
            answer.append(find_index2(val))
        else:
            answer.append(val)    
    for i in answer:
         result.append(alpha[i])           
print(''.join(result))            
print(result)