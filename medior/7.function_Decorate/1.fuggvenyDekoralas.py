def validateDiv(func):
    def wrapper(value1, value2):
        if value2 == 0:
            return "Can not divide by zero"
        return func(value1, value2)
    return wrapper

@validateDiv
def divide(value1, value2):
    return value1 / value2

print(divide(4,7))
print(divide(4,0))

def validateForm(func):
    def wrapper(password,email):
        if len(password) < 6:
            return "Weak password, at least 6 characters"
        if "@" not in email:
            return "Not valid email"
        return func(password,email)
    return wrapper

@validateForm
def form(password, email):
    return "Your password is strong and you have a valid email."

print(form("1234", "almagmail.com"))
print(form("1234567", "almagmail.com"))
print(form("1234567", "alma@gmail.com"))