data =  [8,1,7,9,0,2,22,4,6,5,10]


for i in range(1, len(data)):
   key = data[i]
   j = i - 1
   while j >= 0 and data[j] > key:
      data[j+1] = data[j]
      j -= 1

   data[j +1] = key
print(data)
