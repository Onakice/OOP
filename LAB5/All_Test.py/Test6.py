# def outer_func():
#     x = 6
#     def inner_func():
#         print("Value of x from inner::",x)

#     return inner_func

# out = outer_func()
# out()

# def outer_func(a):

#     def inner_func():
#         print("Value of a from inner::",a)
#     return inner_func

# inner = outer_func(90)
# inner()
# inner2 = outer_func(200)
# inner2()

def outer_func(a):

    def inner_func(b):
        print("Value of a from inner::",a)
        print("Value of b passed to inner::",b)

    return inner_func

inner = outer_func(90)
inner(200)
inner(90)