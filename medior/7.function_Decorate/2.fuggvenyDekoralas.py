def validateEmail(func):
    def wrapper(password, email):
        if "@" not in email:
            return "Not valid email"
        return func(password,email)
    return wrapper

def validatePassword(func):
    def wrapper(password, email):
        if len(password) < 6:
            return "Weak password, at least 6 characters"
        return func(password,email)
    return wrapper

@validateEmail
@validatePassword
def form(email, password):
    return "Your password is strong and you have a valid email."

print(form("1234567", "almagmail.com"))
print(form("1234567", "alma@gmail.com"))
print(form("1234", "alma@gmail.com"))