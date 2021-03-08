from django.shortcuts import render


# Create your views here.

def calculate(request, num1, action, num2):
    data = ''
    if action == '+':
        res = num1 + num2
        data = f'{num1} + {num2} = {res}'
    elif action == '-':
        res = num1 - num2
        data = f'{num1} - {num2} = {res}'
    elif action == '*':
        res = num1 * num2
        data = f'{num1} * {num2} = {res}'
    elif action == 'div':
        res = num1 / num2
        data = f'{num1} / {num2} = {res}'
    else:
        data = 'wrong'
    return render(request, 'calculate/calculate.html', {'data': data})
