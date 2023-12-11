# boolean
user_value = input("Enter the value: ")
is_authenticated = user_value.lower() == "true"
print(type(is_authenticated))
#  why the input value is giving True even we are passing the inputs as False
if is_authenticated:
    print(type(is_authenticated))
    print("Welcome to the library you are allowed")
else:
    print("You are not allowed for the library")
# condition true or false
a= 1000
b= 320
if b > a:
    print("b greater than a")
else:
    print("b is not greater than a ")