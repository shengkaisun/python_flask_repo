print(1 >= 2)
print(1 == 2)
print(1 != 3)
username = 'Admin'
check = 'Admin'
print(username == check)

print(1 == 1 and 2 < 3)
print(1 == 2 or 2 < 3)

if 1 > 2:
    print('Yep')
elif 1 == 1:
    print('Ah')
elif 2 != 3:
    print('Great')
else:
    print('Nope')

mylist = [1, 2, 3, 4, 5]
for item in mylist:
    print(item**2)

salaries = {'John': 10, 'Sally':20, 'Lisa':30}
for employee in salaries:
    print(f"{employee}'s salary is {salaries[employee]}")

mypairs = [('a', 1), ('b', 2), ('c', 3)]
# unpack the tuple in  for loop
for letter, num in mypairs:
    print(letter)

i = 1
while i < 5:
    print(f"i is {i}")
    i += 1

for x in range(0,5):
    print(x)

result =  list(range(0, 11, 2))

# in keyword by itself -- return boolean
print('s' in 'ipsumxfsafasfwerwradsfdsklhjlk')

###############
# Functions
###############
# Default value arg = sth
def report_person(name='Blank'):
    print("reporting " + name)

report_person('Cindy')
report_person()

def add_num(num1, num2):
    return num1 + num2

result = add_num(2, 4)
print(result)

# max and min
print(max(2, 3))
print(min([1, 3, 4, 5, 7, 10]))
# enumerate
mylist = ['a', 'b', 'c']
for index, item in enumerate(mylist):
    print(index, item)

# join list
mylist = ['a', 'b', 'c', 'd']
print('--'.join(mylist))

# Return boolean
def secret_check(mystring):
    return 'secret' in mystring.lower()
print(secret_check('this is a Secret'))

# code maker function
def code_maker(mystring):
    for letter in mystring:
        for vowel in 'aeiou':
            if letter == vowel:
                print(letter)

code_maker('Sammy')

def finding_vowel(string):
    s = ''
    for c in string:
        if c.lower() in 'aeiou':
            s += 'x'
        else:
            s += c
    return s

print(finding_vowel('Jerry Sun'))