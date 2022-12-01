print("Hello World")
print("Jatin katyal")
print(isinstance('a',int))
a='a'
print(type(a))
print(isinstance(print,object))
print(hex(id(a)))
a=200
print(hex(id(a)))
b=200
print(hex(id(b)))
b=278
print(hex(id(b)))
c=278
print(hex(id(c)))
b='aaaaa'
print(id(b))
a=2323525020235325016323123136503240531523032036415201231351423501524
print(a+1)
_a=12
print(_a)
print(1)
print(1,2,3, "jatin", 3.4, 2 + 5j, sep=",")
print("Hello", end=";")
print("World :")
print('a', end=")")
print('b')
print('c')
a=input()
b=input()
print(a)
print(b)
print(type(a))
print(int(65))
print(bin(65))
a= 15
print(str(a))
print(int('1234'))
print(float(1.2))
a=67
print(isinstance(a, object))
a='A'
print(isinstance(a, object))
print(5 + 5)
print(10 - 5)
print(isinstance(10.0, int))
print(10/3)
print(10//3)
print(10%3)
print(2**3)
print("jatin" + "katyal")
print("abc" * 6)
print("jatin" " " "katyal")
print(1==2)
print(1<2)
print(1>2)
print("ab" < "z")
print(True and False)
print(True or False)
print(True and 1)
print(0 and 1)
print(1 and 5)
print(isinstance(True, int))
print(type(True))
print(bool(0))
print(bool(""))
print(bool((1,2,3)))
print("" and 0)

a=False
if True:
    print("this value is true")
print("end")

b=False
if b:
    print("this value is true")
else:
    print("this value is false")

a=5
if a==3:
    print("this value is 3")
elif a==5:
    print("this is 5")
else:
    print("this value is 3 or 5")

a = 1
while a< 10:
    print(a)
    a += 1

print(iter("shygyudhyh"))

a= "jatin"
print(a.__iter__)

name = "Shivam"
print(type(name))
print("***")

for c in name:
    print(c)
    print(type(c))
for i in range(len(name)):
    print(i)
a=range(6)
print(a)
for i in range(len(name)):
    if i == 3:
        continue
    print(i)
for i in range(len(name)):
    if i == 3:
        break
    print(i)
for i in range(6):
    print(i)
    del i
for i  in [0,1,2,3,4,5]:
    print(i)
    i=100
    print(i)
if True:
    pass
print("rest of the code")

for i in range(6):
    print(i)
    if i==3:
        break
else:
    print("something")
n = 5
for i in range(n):
    for j in range(n):
        print(i)
    print()
    n = 5
for i in range(n):
    for j in range(n):
        print(i, end=" ")
n = 5
for i in range(n):
    for j in range(n):
        print(i, end=" ")
    print("\n")
n = 5
for i in range(n):
    for j in range(n):
        print(n-i, end=" ")
    print()
    n = 5
for i in range(n):
    for j in range(n):
        print(n-j, end=" ")
    print()
print(max(1 ,2, 3, 4, 5, 7))
n=9
for i in range(n):
    for j in range(n):
        print(max(i+1, j+1, n-i, n-j), end=" ")
    print()
n=9
for i in range(n):
    for j in range(n):
        print((i,j), end=" ")
    print()
n = 5
for i in range(n):
    for j in range(n):
        print(i, end=" ")
    print()
n = 5
for i in range(n):
    for j in range(n):
        print(j, end=" ")
    print()