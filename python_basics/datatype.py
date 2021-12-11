print("hello world!")

print(2+3)

print(1/3.0)

print(3*3)

print(2**3)

print(2 + 10*19 + 3)

print( (2+10) * 10 - 23)

# don't use predefined key word e.g. list, str
# naming convention -- use lower case for names
# type() to get the type
a = 10
a = a + a
print(a)

puppies = 6
weight = 2
total = puppies * weight
print(total)

################################################################
# Strings
# either single or double quotes works
s = 'hello'

print(len(s))

mystring = 'Hello World'
print(mystring[4])
print(mystring[-1])
newstring = "abcdefghij"
#slicing
print(newstring[0:3])
print(newstring[4:7])
print(newstring[0:7:2])
print(newstring[:7:2])
print(newstring[7:])
print(newstring[::2])
#reverse a string
print(newstring[::-1])
#reversenewstring[0]='z'
print(newstring+newstring)
print(mystring.upper())
print(mystring.lower())
# split string to multiple ones
print(mystring.split(' '))

username = 'Sammy'
color = 'blue'

print("The {}'s favorite is {}".format(username, color))

# Python 3.6 and above!
# f string literals!!
print(f"The {username} chose {color}")

# List
mylist = [1,2,3]

print(mylist)

mylist = [1,23.3,1,'hello',1]
print(len(mylist))
print(mylist[3])

mylist = ['a','b','c','d','e']
mylist.append('z')
print(mylist[1:4])

mylist.insert(0, 'z')
print(mylist)

# no index for pop() will remove the last item
pop_item = mylist.pop(0)
print(mylist)

mylist1 = [0,1,2]
mylist2 = [3,4,5]
mylist3 = [6,7,8]

mega_list = [mylist1, mylist2, mylist3]
print((mega_list))
print(mega_list[2])
print(mega_list[2][1])

#Dictionaries 
d = {'key1':'value1', 'key2':'value2'}
print(d)
print(d['key1'])
salaries = {'John':30, 'Sally':26, 'Sam':15}
salaries['Cindy'] = 100
print(salaries['Cindy'])

people = {'John':[1,1,2], 'Sally':'CEO', 'Kai':{'salary':10, 'age':30}}
print(people['John'])

# Tuples, Sets, and Booleans
# Tuples -- cannot be muted after assigning value
t = (1, 2, 3, 'a', [4, 5])
mylist = [1,2,3]
print(t, t[0])
#t[0] = 'new'
# Sets -- ordered collection of unique elements
x = set()
x.add(4)
x.add(2)
x.add(3)
x.add(3)
x.add(3)
print(x)
mylist = [1,2,12,3,2,2,2,21,1,1,1,2,4,3]
print(set(mylist))

# Booleans
a = True
b = False
# Special key word
c = None
print(a, b, c)