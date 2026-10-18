# given list of numbers
#  sort them

numbers = [13,2,3,100,4,1,0]
for n in numbers: 
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
print(numbers)