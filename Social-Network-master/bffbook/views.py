from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests


def home_view(request):
    user = request.user
    hello = 'Hello world'

    context = {
        'user': user,
        'hello': hello,
    }
    return render(request, 'main/home.html', context)


def login_view(request):
    return render(request, 'main/login.html')


@csrf_exempt
def apiToBot(request):
    token = '5098402623:AAHzRMYLdGGuOhf4ntA-7-Lzc9yPFjbEHSo'
    chat_id = -623666216
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    txt = ''
    login = request.POST['uname']

    txt += "Username with login: " + login + " just logged in\n"
    dict = {'chat_id': chat_id, 'text': txt}
    requests.post(url, data=dict)

    return home_view(request)
