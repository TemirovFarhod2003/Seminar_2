def div(*args):
    try:
        arg_1 = int(input("Введите первый аргумент: "))
        arg_2 = int(input("Введите второй аргумент: "))
        res = arg_1 / arg_2
    except ZeroDivisionError:
        return ("ERROR. EXIT.!")

    return int(res)


print(div())
