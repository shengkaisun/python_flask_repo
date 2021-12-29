# python one.py

def foo():
    print("foo in one.py")

print("Top level one.py")

# check if the script is directly run
if  __name__ == "__main__":
    print('One.py is being run directly')
else:
    foo()
    print('one.py has been imported')