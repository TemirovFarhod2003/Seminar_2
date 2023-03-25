def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        print (arg1 + arg2)
    elif arg1 >= arg2 and arg1 >= arg3:
        print (arg1 + arg3)
    else:
        print (arg2 + arg3)

my_func(10,20,20)
