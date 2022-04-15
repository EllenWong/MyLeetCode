# a = [1,2,3,4,5,6]
# b = [0,1,2,3,4,5]
# c = [4,5,6,7,8,9]
#判断组成的数字个数
a = [1,2,3,4,5,6]
b = [0,1,2,7,8,9]
c = [3,4,5,6,7,8]

cout = 0
s = set()

for i in range(6):
    for j in range(6):
        for k in range(6):
            if a[i]*100+b[j]*10+c[k] not in s :
                s.add(a[i]*100+b[j]*10+c[k])
            if a[i]*100+c[j]*10+b[k] not in s:
                s.add(a[i]*100+c[j]*10+b[k])
            if b[i]*100+a[j]*10+c[k] not in s :
                s.add(b[i]*100+a[j]*10+c[k])
            if b[i]*100+c[j]*10+a[k] not in s:
                s.add(b[i]*100+c[j]*10+a[k])
            if c[i]*100+a[j]*10+b[k] not in s :
                s.add(c[i]*100+a[j]*10+b[k])
            if c[i]*100+b[j]*10+a[k] not in s:
                s.add(c[i]*100+b[j]*10+a[k])

for i in range(6):
    for j in range(6):
        if a[i] *10 +b[j] not in s:
            s.add(a[i] *10 +b[j])
        if a[i] *10 +c[j] not in s:
            s.add(a[i] *10 +c[j])
        if b[i] *10 +a[j] not in s:
            s.add(b[i] *10 +a[j])
        if b[i] *10 +c[j] not in s:
            s.add(b[i] *10 +c[j])
        if c[i] *10 +a[j] not in s:
            s.add(c[i] *10 +a[j])
        if c[i] *10 +b[j] not in s:
            s.add(c[i] *10 +b[j])
        
for i in range(6):
    if a[i] not in s:
        s.add(a[i])
    if b[i] not in s:
        s.add(b[i])
    if c[i] not in s:
        s.add(c[i])

print(len(s))