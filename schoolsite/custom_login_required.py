

def login_required(func):
    def wrapper():
        func()

    return wrapper