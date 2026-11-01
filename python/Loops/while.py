students = {
    "John": {
        "math": 85,
        "physics": 78,
        "chemistry": 92
    },

    "Mary": {
        "math": 90,
        "physics": 88,
        "chemistry": 95
    },

    "Peter": {
        "math": 65,
        "physics": 72,
        "chemistry": 60
    },

    "Alice": {
        "math": 95,
        "physics": 91,
        "chemistry": 89
    }
}

for name, grades in students.items():
    sum = 0
    averages = {}
    print(f"\n--- {name}'s Grades ---")

    for subject, score in grades.items():
        sum += score
        print(f"{score}")
    average =  sum/ len(grades) 
    
    averages = {
        name[i]: average[i] for i in range(len(students))
    }
    print(averages)
        
