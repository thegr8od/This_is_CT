n = int(input())

data = []
for i in range(n):
    input_data = input().split()
    data.append((input_data[0], int(input_data[1])))

result = sorted(data, key=lambda student: student[1])

for i in result:
    print(i[0], end=' ')