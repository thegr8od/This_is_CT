n,m = map(int, input().split())

min_value = 0
min_lst = []
for i in range(n):
    lst = list(map(int, input().split()))
    if min(lst)>min_value:
        min_value = min(lst)
    #min value = min(data)
    #min_value = max(min_value, min(lst))

print(min_value)

