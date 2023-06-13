import re
import math
# from core import SmartCalc as sc

def parse_expression(expression):
    # Используем регулярное выражение для разделения строки на числа, операции и скобки
    pattern = r"(\s*sin\s+" \
              r"|\s*cos\s+" \
              r"|\s*acos\s+" \
              r"|\s*asin\s+" \
              r"|\s*ln\s+" \
              r"|\s*log\s+" \
              r"|\s*tan\s+" \
              r"|\s*atan\s+" \
              r"|\s*sqrt\s+" \
              r"|[\d.]+|\+|\-|\%|\*|/|\(|\))"
    tokens = re.findall(pattern, expression)

    # Формируем словарь токенов
    dict = ('+', '-', '*', '/', '%',
            'sin ', 'cos ', 'acos ', 'asin ',
            'ln ', 'log ', 'tan ', 'atan ', 'sqrt ')
    # Создаём пустой стек
    stack = []

    # Создаём пустой список для хранения чисел и операций
    output = []

    # Определяем приоритеты операций
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    # Обрабатываем каждый токен в выражении
    for token in tokens:
        if token.isdigit() or '.' in token:
            # Если токен является числом, добавляем его в выходной список
            output.append(float(token))
        elif token.strip() in dict:
            # Если токен является операцией
            while stack and stack[-1] != '(' and precedence[token] <= precedence.get(stack[-1], 0):
                # Проверяем приоритет текущей операции относительно операций в стеке
                output.append(stack.pop())
            stack.append(token.strip())
        elif token in dict:
            # Если токен есть в словаре токенов, добавляем его в стек
            stack.append(token.strip())
        elif token == '(':
            # Если токен является открывающей скобкой, добавляем его в стек
            stack.append(token.strip())
        elif token == ')':
            # Если токен является закрывающей скобкой
            while stack and stack[-1] != '(':
                # Перемещаем операции из стека в выходной список, пока не встретим открывающую скобку
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                # Удаляем открывающую скобку из стека
                stack.pop()

    # Добавляем оставшиеся операции из стека в выходной список
    while stack:
        output.append(stack.pop())

    return output


def evaluate_expression(tokens):
    stack = []
    operations = ('+', '-', '*', '/', '% ')
    functions = ('sin', 'cos', 'acos', 'asin',
                 'ln', 'log', 'tan', 'atan', 'sqrt')

    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token in operations:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '-':
                result = operand1 - operand2
            elif token == '+':
                result = operand1 + operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            elif token == '%':
                result = operand2 * (operand1 / 100)
            stack.append(result)
        elif token in functions:
            func = token.strip()
            operand = stack.pop()
            if func == 'sin':
                result = math.sin(operand)
            elif func == 'cos':
                result = math.cos(operand)
            elif func == 'acos':
                result = math.acos(operand)
            elif func == 'asin':
                result = math.asin(operand)
            elif func == 'ln':
                result = math.log(operand)
            elif func == 'log':
                result = math.log10(operand)
            elif func == 'tan':
                result = math.tan(operand)
            elif func == 'atan':
                result = math.atan(operand)
            elif func == 'sqrt':
                result = math.sqrt(operand)
            stack.append(result)

    return stack.pop()


# def result_display(value):
#     string = str(value)
#     num = string.split(".")
#     if num[1] == "0":
#         return int(num[0])
#     else:
#         return value

def main():
    expression = "log 3"
    parsed_tokens = parse_expression(expression)
    result = evaluate_expression(parsed_tokens)
    # result = result_display(result)
    print(result)


if __name__ == '__main__':
    main()
