import os
import json
from django.shortcuts import render

from .models import Users

# Create your views here.

name = 'max'

db_path = os.path.join('calculate', 'db.json')


def home(request):
    return render(request, 'calculate/home.html', {'name': name})


def users(request):
    with open(db_path, 'r') as file:
        users_list = [Users(**item) for item in json.load(file)]
    return render(request, 'calculate/users.html', {'users': users_list})


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
        res = num1 // num2
        data = f'{num1} // {num2} = {res}'
    else:
        data = 'wrong'
    return render(request, 'calculate/calculate.html', {'data': data})
