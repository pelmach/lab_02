n = int(input())

mas = []
for i in range(n + 1):
    mas.append(i)

mas[1] = 0
i = 2

while i <= n:
    if mas[i] != 0:
        j = i + i
        while j <= n:
            mas[j] = 0
            j = j + i
    i += 1

mas = set(mas)
mas.remove(0)
print(mas)