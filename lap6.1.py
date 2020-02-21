data = []

while(True):
    data.clear()
    data = input().split()
    if (len(data) > 20) or (len(data) < 2):
        print("Data input overload")
    else:
        break

for i in range(len(data)):
    data[i] = int(data[i])

data.sort()
avg = sum(data)/len(data)

temp1 = [] #hight
temp2 = [] #low

for i in range(len(data)):
    if data[i] >= avg:
        temp1.append(data[i])
    else:
        temp2.append(data[i])


print("{:.2f}".format(sum(temp1)/len(temp1)))
print("{:.2f}".format(sum(temp2)/len(temp2)))