#making all the text upper case

def change(func):
    def inner():
        return func().upper()
    return inner

@change
def myfunc():
    return 'hello jubaer'

print(myfunc())