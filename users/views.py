from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from annoying.functions import get_object_or_None
import json

from django.views.decorators.csrf import csrf_exempt

from users.models import UserToken
from utilities import Token

@csrf_exempt
def index(request):
    response = {
        "threat": "easter egg ahora debes darme tu numero de tarjeta, fecha de caducidad y cvv"
    }
    return JsonResponse(response)


@csrf_exempt
def login(request):
    try:
        data = json.loads(request.POST["data"])
        username = data.get("username")
        password = data.get("password")

        # -- user and pswd checking --
        if (username is None and password is None) or (username == "" and password == ""):
            return JsonResponse({
                "result": "error",
                "message": "user and password are empty or none"
            })

        if username is None or username == "":
            return JsonResponse({
                "result": "error",
                "message": "user is empty or none"
            })

        if password is None or password == "":
            return JsonResponse({
                "result": "error",
                "message": "password is empty or none"
            })
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
                    print(user.username + "logged in")
                    response_data = {
                        "result": "ok",
                        "username": user.username,
                        "email": user.email,
                        "token": user_token.token
                    }
                    return JsonResponse(response_data)

        else:
            return JsonResponse({
                "result": "error",
                "message": "no user"
            })

    except Exception as e:
        return JsonResponse({
            "result": "error",
            "message": "something went wrong on the server",
            "traceback": str(e)
        })


@csrf_exempt
def logout(request):
    try:
        token = request.POST["token"]

        if (token is None) or (token == ""):
            return JsonResponse({
                "result": "error",
                "message": "token was empty or none"
            })

        user_token = get_object_or_None(UserToken, token=token)

        if user_token is None:
            return JsonResponse({
                "result": "ok",
                "message": "user was already logged out"
            })
        else:
            user_token.delete()
            return JsonResponse({
                "result": "ok",
                "message": "succesfully logged out"
            })

    except Exception as e:
        print(e)
        return JsonResponse({
            "result": "error",
            "message": "something went wrong on the server",
            "traceback": e.__traceback__
        })


@csrf_exempt
def signup(request):
    try:
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")

        # -- user and pswd checking --
        if username is None or username == "":
            return JsonResponse({
                "result": "error",
                "message": "user is empty or none"
            })

        if email is None or email == "":
            return JsonResponse({
                "result": "error",
                "message": "email is empty or none"
            })

        if password is None or password == "":
            return JsonResponse({
                "result": "error",
                "message": "password is empty or none"
            })
        # -- end of user and pswd checking --

        user = User.objects.create_user(username, email, password)
        user.save()

        return JsonResponse({
            "result": "ok",
            "message": "user was created succesfully"
        })

    except Exception as e:
        return JsonResponse({
            "result": "error",
            "message": "something went wrong on the server",
            "traceback": e.__traceback__
        })

