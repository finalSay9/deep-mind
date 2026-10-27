data = [8,1,7,9,0,2,4,6,5]


for _ in range(len(data)):
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]

print(data)