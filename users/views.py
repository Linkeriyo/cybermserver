from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from annoying.functions import get_object_or_None
import json

from django.views.decorators.csrf import csrf_exempt


def index(request):
    response = {
        'threat': 'easter egg ahora debes darme tu numero de tarjeta, fecha de caducidad y cvv'
    }
    return JsonResponse(response)


@csrf_exempt
def login(request):
    print(request.body)

    try:
        datos = json.loads(request.body)
        username = datos.get('username')
        password = datos.get('password')
        user = get_object_or_None(User, username=username)

        response = {
            "username": user.username,
            "email": user.email
        }

        if (username is None and password is None) or (username == "" and password == ""):
            response = {
                "result": "error",
                "message": "user and password are empty or none"
            }
            return JsonResponse(response)

        if username is None or username == "":
            response = {
                "result": "error",
                "message": "user is empty or none"
            }
            return JsonResponse(response)

        if password is None or password == "":
            response = {
                "result": "error",
                "message": "password is empty or none"
            }
            return JsonResponse(response)

        user = auth.authenticate(username=username, password=password)
        user.save()
        # TODO: me queda un huevo



    except Exception as e:
        return JsonResponse(response)
