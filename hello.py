def Method():
    print("This is a second method call!")

def Hello():
    print("Hey there! This is a method, it is pretty useless if you ask me!")
    Method()

if __name__ == '__main__':
    Hello()
