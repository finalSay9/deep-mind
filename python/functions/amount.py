def calculate(*amount):
    total = 0
    for i in amount:
        total += i
    return total

result = calculate(1000,3000,5000,8000,10000)
print(result)

#positional keyword arguments

def createUser(**detail):
    print(detail)


createUser(
    name="evan",
    age=24,
    email="evan@gmil.com",
    password="evn1234"
)