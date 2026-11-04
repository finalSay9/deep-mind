password = "evan1234"


attempt = 1

while attempt <= 4:
    print("\nenter your password")
    pwd = input("")
    if pwd == password:
        print("correct pasword")
    elif pwd != password:
        if attempt == 3:
                print("system shutdown temporaliry")
        print("incorect password try again")
    else:
        if attempt == 3:
            print("system shutdown temporaliry")
    attempt += 1
