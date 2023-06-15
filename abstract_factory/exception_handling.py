'A simple program to play with exception handling'

#This will show how you can raise your own exceptions
name = input("what is your name?\n")

try:
    if name == 'bob':
        print("Hello bob!")
    elif name == "alice":
        print("Hello alice!")
    else:
        raise Exception('Sorry no hello for you!')
except Exception as _e:
    print(_e)

#this will show how to use built-in exceptions
try:
    print(variable_not_declared)
except NameError:
    print("We just caught the standard NameError when a variable is not declared.")
except:
    print("Variable not found!")
finally:
    print("This is optional and will run even if there aren't errors!")

