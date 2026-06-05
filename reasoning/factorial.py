#writing an algorithim that calculates the factorial of any given number

def facto(number: int):
    #base cases 0 and 1
    if number == 0 or number == 1:
        return 1
    else:
        return number * facto(number -1)


#desired = int(input('enter the number'))
result = facto(10)

print(result)