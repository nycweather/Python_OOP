def outer(func):
    print("Accessing :", outer.__name__)
    def inner():
        print("Accessing :", func.__name__)
    return inner



@outer
def greet():
    return 'Hello!'

greet()


