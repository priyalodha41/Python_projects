def decorator_function(orginal_function):
    def wrapper_function(*args,**kwargs):
        print(f"Wrapper executed before the {orginal_function.__name__.lower()} function");
        return orginal_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display():
    print("Display Function just ran");

display();

@decorator_function
def display_info(name,age):
    print(f'Display_info ran with arguments ({name},{age})')
    
display_info("John",27)
# decorated_display=decorator_function(display);
# decorated_display();