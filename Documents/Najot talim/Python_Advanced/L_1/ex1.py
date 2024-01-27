s = input('Insert text: ')
unlilar = 'aiuoe'

count = 0
for i in s:
    if i not in unlilar:
        count += 1
        if count == 3:
            print("NO")
            break
    else:
        count = 0
else:
    print('YES')