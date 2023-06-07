from django.shortcuts import render


def calculator(request):
    return render(request, 'calculator.html')


def calculate(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operator = request.POST['operator']

        result = 0

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2

        return render(request, 'calculator.html', {'result': result})
    else:
        return render(request, 'calculator.html')


def calc(request):
    return render(request, 'index.html')