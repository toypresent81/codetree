arr = list(map(int, input().split()))
odd = arr[0::2]
even = arr[1::2]
odd_sum = sum(odd)
even_sum = sum(even)
if odd_sum > even_sum:
    print(odd_sum - even_sum)
else:
    print(even_sum - odd_sum)