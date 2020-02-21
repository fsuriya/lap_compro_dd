x = int(input())

i = 0
j = 1

if x >= 1:
    print(0)
    
if x >= 2:
    print(1)

for y in range(x-2):
    a = i+j
    print(a)
    i = j
    j = a 
