# using *args makes the function to be able to receive variable arguments
# args itself is a tuple of arguments, therefore it can be iterated over
def flexible_function_arguments(*args):
    print(f"{type(args)}")
    for arg in args:
        if isinstance(arg, str):
            print(f"{arg.upper()} - {type(arg)}")
        elif isinstance(arg, list):
            arg.reverse()
            print(f"{arg} - {type(arg)}")
        else:
            print(f"{arg} - {type(arg)}")

# In contrast, **kwargs makes the function to be able to receive variable keyword arguments
# The keyword arguments are stored in a dictionary, so can be accessed by their key/name


def flexible_function_keyword_arguments(**kwargs):
    print(f"-----\n{kwargs}")
    print(f"{type(kwargs)}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def configure(host, port, timeout=10):
    print(f"Connecting to {host}:{port} (timeout={timeout})")


flexible_function_arguments("Hello", "World", 123, True,
                            12.364, [1, 2, 3], {"name": "John"})

# Each parameter will be interpreted as an element of the dictionary
flexible_function_keyword_arguments(name="John", age=30, city="New York")

# Unpacking arguments is also possible using * or **
settings_list = ["example.com", 8080, 30]
settings_dict = {"host": "example.com", "port": 8080, "timeout": 30}
configure(*settings_list)
configure(**settings_dict)
