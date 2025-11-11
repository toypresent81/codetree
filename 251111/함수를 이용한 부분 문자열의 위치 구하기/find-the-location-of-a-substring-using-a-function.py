text = input()
pattern = input()

def checkInString():
    index = -1
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            index = i
            break
    return index


print(checkInString())