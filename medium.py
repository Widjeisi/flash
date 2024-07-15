a = str(input())
b = str(input())
c = '' #это будет новая строка

i, j = 0, 0

while (i < len(a)) and (j < len(b)):
    if ord(a[i]) <= ord(b[j]):
        c += a[i]
        i += 1
    else:
        c += b[j]
        j += 1


#все остатки после конца одной из строк просто закидываем
if (i >= len(a)):
    while j < len(b):
        c += b[j]
        j += 1

else:
    while i < len(a):
        c += a[i]
        i += 1

cnt = 1 #текущее количество символов в проверяемой последовательности
ans = 0 #ответ

for i in range(1, len(c)):
    if ord(c[i - 1]) <= ord(c[i]):
        cnt += 1
        ans = max(ans, cnt)
    else:
        ans = max(ans, cnt)
        cnt = 1

print(ans)
