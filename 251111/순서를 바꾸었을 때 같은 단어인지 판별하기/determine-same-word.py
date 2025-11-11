word1 = input()
word2 = input()

word1_arr = list(word1)
word2_arr = list(word2)
word1_arr.sort()
word2_arr.sort()

print("Yes" if word1_arr == word2_arr else "No")
