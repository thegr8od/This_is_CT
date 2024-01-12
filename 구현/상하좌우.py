n = int(input())

x = 1
y = 1

data = list(input().split())

for i in data:
    if i == 'R':
        if y < n:
            y += 1
        else:
            continue
    elif i == 'L':
        if y > 1:
            y -= 1
        else:
            continue
    elif i == 'U':
        if x > 1:
            x -= 1
        else:
            continue
    else:
        if x < n :
            x += 1
        else:
            continue

print(x,y)
