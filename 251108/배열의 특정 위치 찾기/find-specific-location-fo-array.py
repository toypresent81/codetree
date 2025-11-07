arr = list(map(int, input().split()))
even_arr = arr[1::2]
thrid_arr = arr[2::3]
even_sum = sum(even_arr)
third_sum = sum(thrid_arr)
avg = third_sum/len(thrid_arr)
print(f"{even_sum} {avg:.1f}")