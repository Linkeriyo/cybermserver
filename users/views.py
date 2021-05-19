from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from annoying.functions import get_object_or_None
import json

from django.views.decorators.csrf import csrf_exempt

from users.models import UserExtraData, UserToken
from utilities import Token

@csrf_exempt
def index(request):
    return JsonResponse({
        "threat": "cuidado"
    })


def check_user(token, username):
    try:
        user_token = get_object_or_None(UserToken, token=token)

        if user_token is None:
            return {
                "result": "error",
                "message": "token is null"
            }

        if user_token.user.username != username:
            return {
                "result": "error",
                "message": "token does not match with username"
            }

        return {
            "result": "ok",
            "message": "token is valid"
        }

    except Exception as e:
        return {
            "result": "error",
            "message": str(e)
        }


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
            
                return JsonResponse({
                    "result": "ok",
                    "username": user.username,
                    "email": user.email,
                    "token": user_token.token
                })

            else:
                return JsonResponse({
                    "result": "error",
                    "message": "user is not active"
                })
        
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
        return JsonResponse({
            "result": "error",
            "message": "something went wrong on the server",
            "traceback": str(e)
        })


@csrf_exempt
def signup(request):
    try:
        data = json.loads(request.POST['data'])
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

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
            "result": "ok", "message": "user was created succesfully"
        })

    except Exception as e:
        return JsonResponse({
            "result": "error",
            "message": "something went wrong on the server",
            "traceback": str(e)
        })

@csrf_exempt
def check_user_extra_data(request):
    try:
        data = json.loads(request.POST['data'])
        token = data.get('token')
        username = data.get('username')

        check_result = check_user(token, username)

        if check_result.get('result') != 'ok':
            return JsonResponse(check_result)

        user_token = get_object_or_None(UserToken, token=token)
        user = user_token.user

        user_extra_data = get_object_or_None(UserExtraData, user=user)

        if user_extra_data is None:
            return JsonResponse({
                "result": "ok",
                "has_extra_data": False
            })
        
        else:
            return JsonResponse({
                "result": "ok",
                "has_extra_data": True,
                "user_extra_data": user_extra_data.json()
            })

    except Exception as e:
        return JsonResponse({
            "result": "error",
            "message": "something went wrong on the server",
            "traceback": str(e)
        })


@csrf_exempt
def set_user_extra_data(request):
    try:
        data = json.loads(request.POST['data'])
        token = data.get('token')
        username = data.get('username')
        name = data.get('name')
        surname = data.get('surname')
        phono = data.get('phono')
        address = data.get('address')
        city = data.get('city')
        province = data.get('province')
        zip_code = data.get('zip_code')

        check_result = check_user(token, username)
        if check_result.get('result') != 'ok':
            return JsonResponse(check_result)
        
        user_token = get_object_or_None(UserToken, token=token)
        
        user_extra_data = UserExtraData(
            user=user_token.user, 
            name=name, surname=surname,
            phono=phono, address=address,
            city=city, province=province,
            zip_code=zip_code
        )
        user_extra_data.save()
        
        return JsonResponse({
            "result": "ok",
            "message": "extra_data was created succesfully",
            "user_extra_data": user_extra_data
        })

    except Exception as e:
        return JsonResponse({
            "result": "error",
            "message": "something went wrong on the server",
            "traceback": str(e)
        })