st = str(input())
check = []   #имеющиеся символы
ans = 0

for i in range(len(st)):
    if not ((ord(st[i]) >= 65 and ord(st[i]) <= 90) or (ord(st[i]) >= 97 and ord(st[i]) <= 122)):
        if not ord(st[i]) in check:
            check.append(ord(st[i]))
            ans += 1

print(ans)
