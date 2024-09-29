import time

def mainDecorator(state):
    def validateForm(func):
        def wrapper(password,email):
            print(state)
            time.sleep(1)
            if len(password) < 6:
                return "Weak password, at least 6 characters"
            if "@" not in email:
                return "Not valid email"
            return func(password,email)
        return wrapper
    return validateForm

@mainDecorator("validating...")
def form(password, email):
    return "Your password is strong and you have a valid email."

print(form("1234", "almagmail.com"))
print(form("1234567", "almagmail.com"))
print(form("1234567", "alma@gmail.com"))