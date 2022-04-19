import re
operation_f = ['^', '+', '-', '*', '/']
function_reg = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
reg = r'[^\+\-\*\/\^\.\)\(\d]'


def division(x, y):
    try:
        return str(float(x) / float(y))
    except ZeroDivisionError:
        print(f'ПРОИЗОШЛА ОШИБКА! \n'
              f'В операции: {x}/{y}, на 0 делить нельзя!')


def corrected_task(task):
    task = task.replace('**', '^')
    task = task.replace('pi', '3.14')
    task = task.replace('e', '2.71')
    task = task.replace(' ', '')
    return task


# Cоздаем list с операциями
def created_list_operation(task, operation):
    result = [i for i in task if i in operation]
    return result


# Cоздаем list - items с приоритетами и ф-ями
def created_tuple_operation(operation, dict_priority):
    list_result = []
    for elem in operation:
        if elem in dict_priority:
            tuple_n = (elem, dict_priority[elem])
            list_result.append(tuple_n)
    return list_result


# Разбираем выражения и считаем согласно мат. операций
def func_math_operation(task: str, function):
    for symbol, action in function:
        parsing_operation = re.search(function_reg.format(symbol), task)
        try:
            task: str = task.replace(parsing_operation.group(0), action(*parsing_operation.groups()))
        except TypeError:
            print(f'Ответ может быть неккоректный проверьте ваше выражение!')
        except AttributeError:
            print('')
    return task


#  Разбиваем операции по приоритетам
priority_1 = {'^': lambda x, y: str(float(x) ** float(y))}
priority_2 = {
    '*': lambda x, y: str(float(x) * float(y)),
    '/': division
}
priority_3 = {
    '-': lambda x, y: str(float(x) - float(y)),
    '+': lambda x, y: str(float(x) + float(y))
}

print('          *** КАЛЬКУЛЯТОР ***\n'
      '  возможные операции (+, -, *, /, **)\n'
      'стандартные константы - pi(3.14), e(2.71)')
print('-' * 42)


while True:
    input_task = input('Введите выражение в формате 2+2*2: ')

    input_task = corrected_task(input_task)

    pars_no_value_symbol = re.search(reg, input_task)

    # Проверяем выражение на недопустимые символы
    if pars_no_value_symbol == None:
        operation_task = created_list_operation(input_task, operation_f)

        function_priority_1 = created_tuple_operation(operation_task, priority_1)
        function_priority_2 = created_tuple_operation(operation_task, priority_2)
        function_priority_3 = created_tuple_operation(operation_task, priority_3)

        after_priority_1 = func_math_operation(input_task, function_priority_1)

        after_priority_2 = func_math_operation(after_priority_1, function_priority_2)

        result_finish = func_math_operation(after_priority_2, function_priority_3)

        print(f'Результат: {result_finish}')
    else:
        print('В вашем выражении есть недопустимые символы!')

    print('-' * 42)
    input_question = input('Хотите продолжить?  да(Y) / нет(любая клавиша): ').upper()
    if input_question == 'Y':
        continue
    else:
        print('Программа завершается...')
        break
