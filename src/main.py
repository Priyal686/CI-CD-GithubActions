def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print("Cannot divide by zero:",e)
        return None

def mul(a,b):
    return a*b

if __name__ == '__main__':
    print("App is running")


