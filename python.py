def f(lst):
    try:
        assert len(lst) > 0
        print("List is not empty")
    except AssertionError:
        print("List is empty")
age = int(input("Enter your age: "))

try:
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as e:
    print("Invalid input:", e)
    

try:
    print(10/0)
except ZeroDivisionError:
    print("can divide by zero")
    
try:
    x = int("hello")
except ValueError :
    print("Invalid input:")

try:
    list1 = [1, 2, 3]
    print(list1[5])
except IndexError:
    print("Index out of range")
    
try:
    dic = {'a': 1, 'b': 2}
    print(dic['c'])
except KeyError:
    print("Key not found")

try:
    print("hello" + 5)
except TypeError:
    print("can only concatenate str (not 'int') to str")
    

x = int(input("Enter a number: "))
assert x >= 0


