import ast


def corrected_task(task):
    task = task.replace('pi', '3.14')
    task = task.replace('e', '2.71')
    return task


print('          *** КАЛЬКУЛЯТОР ***\n'
      '  возможные операции (+, -, *, /, **)\n'
      'стандартные константы - pi(3.14), e(2.71)')
print('-' * 42)

while True:
    input_task = input('Введите выражение в формате 2+2*2: ')

    input_task = corrected_task(input_task)

    input_task = f'print({input_task})'

    try:
        parsing_operation = ast.parse(input_task)
        result_finish = compile(parsing_operation, "<string>", "exec")
    except SyntaxError:
        print('В вашем выражении есть недопустимые символы!')
    else:
        print('Результат:')
        try:
            exec(result_finish)
        except ZeroDivisionError:
            print('Ошибка! На 0 делить нельзя!')
        except NameError:
            print('В вашем выражении есть недопустимые символы!')

    print('-' * 42)
    input_question = input('Хотите продолжить?  да(Y) / нет(любая клавиша): ').upper()
    if input_question == 'Y':
        continue
    else:
        print('Программа завершается...')
        break
