a=123980323
b=456789
s1=str(a)
s2=str(b)

l1=len(s1)
l2=len(s2)

t = l1 if l1 < l2 else l2

for i in range(0, t):
    print(s1[i:i+1] + "" + s2[i:i+1], end="")

if l2 < l1:
    print(s1[t:])
else:
    print(s2[t:])

l = [12, 5, 18, 7, 15]
print(max(l))
l.remove(max(l))
print(max(l))
