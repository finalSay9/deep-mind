names = ["Evan", "John", "Mary"]

scores = [95, 80, 90]
highest = scores[0]

for name, score in zip(names, scores):
    if highest > score:
        highest = score
        print(highest)
    