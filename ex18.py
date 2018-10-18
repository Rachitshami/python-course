def print_two(*args):
    arg1, arg2 = args
    print(f"args1: {arg1}, args2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing.")

print_two("RACHIT", "SHAMI")
print_two_again("Rachit", "Shami")
print_one("Rachit")
print_none()
