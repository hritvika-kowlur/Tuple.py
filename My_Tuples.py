
list = [1,2,3,4,5,6]

print(list[0])

list.append(7)

print(list) 

tuple = (1,2,3,4,5,6)

print(tuple)

print(tuple[5])

#tuple.append(7)
#tuples are immutable where as lists are mutable

print(tuple)

tuple = ((1,2,3,4),("Green"),(0.4,0.6,0.8))

print(tuple[1])
print(tuple[0][3])

#slicing
print(tuple[0:2])

#packing
student = ("Hritvika",12,"Computing")

#unpacking
name,age,subject = student
#del student

for i in student:
    print(i)

print("name: ",name)    
print("age: ",age)
print("subject: ",subject)