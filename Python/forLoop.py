# * * * * *
# * * * * *
# * * * * *
# * * * * *
a=5
for i in range(a):
    for j in range(i,a):
        print("*",end=' ')
    print()

for i in range(a):
    for j in range(i,a):
        print(" ",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print()

print("==============")
for i in range(a):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,a):
        print("*",end=' ')
    print()

print("================================")
for i in range(a):
    for j in range(i,a):
        print(" ",end=' ')
    for j in range(i):
        print("*",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print()
print("================================")

for i in range(a):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,a-1):
        print("*",end=' ')
    for j in range(i, a):
        print("*",end=' ')
    print() 

print("================================")

for i in range(a-1):
    for j in range(i,a):
        print(" ",end=' ')
    for j in range(i):
        print("*",end=' ')
    for j in range(i+1):
        print("*",end=' ')
    print() 
for i in range(a):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,a-1):
        print("*",end=' ')
    for j in range(i, a):
        print("*",end=' ')
    print() 