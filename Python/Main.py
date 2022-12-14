# first=input("enter first number :")
# Operato=input("enter first number (+,-,*,%,/) :")
# Second=input("enter Second number :")

# first=int(first)
# Second=int(Second)

# if Operato=="+":
#     print(first+Second)

# elif Operato=="-":
#     print(first-Second)

# elif Operato=="*":
#     print(first*Second)

# elif Operato=="/":
#     print(first/Second) 

# elif Operato=="%":
#     print(first%Second)

# else:print("Invalid operation")



for i in range(10):
    print(i)
print("===============")
marks =[90,75,88]
print(marks[2])

from collections import namedtuple

a=namedtuple('courses', 'name,technology,length')
s=a('DSA','Python','6months')
print(s)

print(True or 0 and false or "abc")

a= ["apple","samsung","oppo","oneplus"]

it=iter(a)

print(it.next)



from collections import hashmap

