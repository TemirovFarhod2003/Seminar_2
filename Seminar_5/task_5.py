def calcul():
    sign = input('Введите 0 : для отмены, + : для сложения, -  : для сложения, *  : для умножения, / : для деления ')

    if (sign == '0'):
        print("Прощайте")
        return

    a = float(input('Введите первое число '))
    b = float(input('Введите второе число '))

    if (sign == '+'):
        print("Сумма чисел = %d" % (a + b))
        return calcul()
    elif (sign == '-'):
        print("разница чисел = %d" % (a - b))
        return calcul()
    elif (sign == '/'):
        if (b == 0):
            print('Делить на ноль нельзя')
            return calcul()
        else:
            print("деление чисел = %.1f" % (a / b))
            return calcul()
    elif (sign == '*'):
        print("Произведение чисел = %d" % (a * b))
        return calcul()
    else:
        print('Нет такой команды')
        return calcul()


print(calcul())