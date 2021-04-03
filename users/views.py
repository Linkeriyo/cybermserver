from django.contrib.auth import authenticate
from django.http import JsonResponse
from annoying.functions import get_object_or_None
import json

from django.views.decorators.csrf import csrf_exempt

from users.models import UserToken
from utilities import Token


def index(request):
    response = {
        'threat': 'easter egg ahora debes darme tu numero de tarjeta, fecha de caducidad y cvv'
    }
    return JsonResponse(response)


@csrf_exempt
def login(request):
    print(request.body)

    datos = json.loads(request.POST['data'])
    username = datos.get('username')
    password = datos.get('password')

    # -- user and pswd checking --
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
    # -- end of user and pswd checking --

    # login
    user = authenticate(username=username, password=password)

    if user is not None:

        if user.is_active:
            user_token = get_object_or_None(UserToken, user=user)

            if user_token is None:
                token_value = Token.generate_value()
                user_token = UserToken(token=token_value, user=user)
                user_token.save()

            else:
                response = {
                    "result": "ok",
                    "username": user.username,
                    "email": user.email,
                    "token": user_token.token
                }
                return JsonResponse(response)
    else:
        response = {
            "result": "error",
            "message": "no user"
        }
        return JsonResponse(response)
