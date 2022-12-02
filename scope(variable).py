
#python #variable #scope

# ========================================================
# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

name = "Steepen" # global scope (available inside & outside functions)

def display_name():
    name = "Raj"    # local scope (available only inside this function)
    print(name)


display_name()
print(name)
