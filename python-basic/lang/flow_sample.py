def loop_with_while(times):
    if times > 0:
        while times > 0:
            print('value is %d' % times)
            times -= 1
    elif times < 0:
        while times < 0:
            print('value is %d' % times)
            times += 1
    else:
        print('value is zero')


def loop_with_foreach():
    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
        print(name)


def loop_with_break_continue():
    names = ['Michael', 'Bob', 'Tracy', 'hzh', 'lm', 'ysl']
    for name in names:
        if name == 'Michael':
            continue

        if name == 'hzh':
            break
        print(name)


def deduce_loop_type(type):
    exeResult = True
    if type == 1:
        value = int(input('input a int:'))
        loop_with_while(value)
    elif type == 2:
        loop_with_foreach()
    elif type == 3:
        loop_with_break_continue()
    elif type == 4:
        exeResult = False
    else:
        pass
    return exeResult

while True:
    type = int(input('input a type with int:'))
    exeResult=deduce_loop_type(type)
    if not exeResult:
        break




