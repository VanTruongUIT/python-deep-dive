# def speak(text):
#     def whisper(t):
#         return t.lower() + '...'
#     return whisper(text)

# print(speak("helle WORLD"))
# speak.whisper("helle WORLD")


# def get_speaker(volume):
#     def whisper(text):
#         return text.lower() + '...'

#     def yell(text):
#         return text.upper() + '!'
    
#     return whisper if volume <= 0.5 else yell

# print(get_speaker(0.7))




# def say_hello(name):
#     return f"Hello {name}"

# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"


# def greet_bob(greeter_func):
#     return greeter_func("Bob")

# print(greet_bob(say_hello))
# print(greet_bob(be_awesome))


# def parent():
    
#     print("Printing from the parent() function")
    
#     def first_child():
#         print("Printing from the first_child() function")
        
#     def second_child():
#         print("Printing from the second_child() function")
        
#     first_child()
#     second_child()
    
# parent()


# def parent(number):
    
#     print("Printing from the parent() function")
    
#     def first_child():
#         return ("Printing from the first_child() function")
        
#     def second_child():
#         return ("Printing from the second_child() function")
        
#     return first_child if number == 1 else second_child
    
# first = parent(1)
# second = parent(2)

# print(first.__name__)
# print(second.__name__)


# ########################### SIMPLE DECORATORS ############################

# def my_decorator(func):
    
#     def wrapper():
#         print("Before call func()")
#         func()
#         print("After call func()")
#     return wrapper


# def say_whee():
#     print("Whee!")


# whee = my_decorator(say_whee)
# print("whee: ", whee)
# whee()


# from datetime import datetime

# This function is called a decorator, because it take a function as an argument and return another function
# def do_not_disturb_the_night(func):
#     def wrapper():
#         current_hour = datetime.now().hour
#         print("current_hour: ", current_hour)
#         if 4 <= current_hour < 7:
#             func()
        
#     return wrapper

# def say_good_morning():
#     print("Good Morning!")

# say_something = do_not_disturb_the_night(say_good_morning)
# say_something()

# Above syntax is a little clunky, so we can use the @ symbol to make it more readable
# def do_not_disturb_the_night(func):
#     def wrapper():
#         current_hour = datetime.now().hour
#         print("current_hour: ", current_hour)
#         if 4 <= current_hour < 7:
#             func()
#         else:
#             print("It's not a good time to say good_morning")
        
#     return wrapper

# @do_not_disturb_the_night
# def say_good_morning():
#     print("Good Morning!")

# say_good_morning()


# from decorators import do_twice


# @do_twice
# def say_something():
#     print(f"Hello World!")

# @do_twice
# def say_twice(name):
#     print(f"Hello World! {name}")



# @do_twice
# def return_from_decorator(name):
#     print("Creating Context")
#     return(f"Hello World! {name}")

# hi = return_from_decorator("David")
# print("hi: ", hi)

    
# print(help(say_something))



# ############################### DECORATORS WITH A FEW REAL WORLD EXAMPLES ############################


# import functools

# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
        
#         value = func(*args, **kwargs)
        
#         # Do something after
        
#         return value

#     return wrapper_decorator

# from decorators import timer

# @timer
# def waste_some_time(num_times):
#     for _ in range(num_times):
#         sum([i**2 for i in range(10000)])


# wash = waste_some_time(999)


# import random

# PLUGINS = dict()


# def register(func):
#     """
#     Register a function as a plugin

#     Args:
#         func (function): function as parameter
#     """
#     PLUGINS[func.__name__] = func
#     return PLUGINS 

# @register
# def say_hello(name):
#     return f"Hello {name}"

# @register
# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"


# def randomly_greet(name):
#     greeter, greeter_func = random.choice(list(PLUGINS.items()))
#     print(f"Using {greeter!r}")
#     return greet_func(name)


############################ DECORATORS IN CLASS ############################
