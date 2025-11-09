a = input()
fruits = ["apple", "banana", "grape", "blueberry", "orange"]
count = 0
for fruit in fruits:
    for idx, char in enumerate(fruit):
        if (char == a and idx == 2) or (char == a and idx == 3):
            count += 1
            print(fruit)
print(count)
