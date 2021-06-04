def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the functions.")
    return wrapper

@announce
def hello():
    print("hello, world!")

hello()