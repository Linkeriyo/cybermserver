from payments.models import CreditCard
from django.http.response import JsonResponse
from users.models import UserCybercafes, UserToken
from businesses.models import CyberCafe
from annoying.functions import get_object_or_None
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def get_methods_by_user(request):
    try:
        token = request.POST["token"]
        
        usertoken = get_object_or_None(UserToken, token=token)
        if usertoken is None:
            return JsonResponse({
                "result": "error",
                "message": "token is null"
            })
                
        cards = CreditCard.objects.filter(user=usertoken.user)
        
        card_list = []
        
        for c in cards:
            card_list.append(c.json())
        
        return JsonResponse({
                "result": "ok",
                "message": "cards retrieved",
                "card_list": card_list
            })
        
    except Exception as e:
        return JsonResponse({
            "result": "error",
            "message": "something went wrong on the server",
            "traceback": str(e)
        })
        
@csrf_exempt
def register_new_card(request):
    try:
        data = json.loads(request.POST["data"])
        card_json = data.get("credit_card")
        token = data.get("token")
        card_holder = card_json.get("card_holder")
        card_number = card_json.get("card_number")
        expires_month = card_json.get("expires_month")
        expires_year = card_json.get("expires_year")
        cvv = card_json.get("cvv")
        
        usertoken = get_object_or_None(UserToken, token=token)
        if usertoken is None:
            return JsonResponse({
                "result": "error",
                "message": "token is null"
            })
            
        credit_card = get_object_or_None(CreditCard,user=usertoken.user, card_number=card_number)
        if credit_card is not None:
            return JsonResponse({
                "result": "error",
                "message": "that card is already added"
            })
        
        credit_card = CreditCard(user=usertoken.user, card_holder=card_holder,
                                 expires_month=expires_month, expires_year=expires_year,
                                 card_number=card_number, cvv=cvv)
        credit_card.save()
        
        return JsonResponse({
            "result": "ok",
            "message": "card has been submitted"
        })
        
    except Exception as e:
        return JsonResponse({
            "result": "error",
            "message": "something went wrong on the server",
            "traceback": str(e)
        })
    

@csrf_exempt
def remove_card(request):
    try:
        data = json.loads(request.POST["data"])
        card_json = data.get("credit_card")
        token = data.get("token")
        card_number = card_json.get("card_number")
        
        usertoken = get_object_or_None(UserToken, token=token)
        if usertoken is None:
            return JsonResponse({
                "result": "error",
                "message": "token is null"
            })
            
        credit_card = get_object_or_None(CreditCard,user=usertoken.user, card_number=card_number)
        if credit_card is None:
            return JsonResponse({
                "result": "error",
                "message": "card is null for user"
            })

        credit_card.delete()
        
        return JsonResponse({
            "result": "ok",
            "message": "card has been deleted"
        })
        
    except Exception as e:
        return JsonResponse({
            "result": "error",
            "message": "something went wrong on the server",
            "traceback": str(e)
        })


@csrf_exempt
def get_cybergold(request):
    try:
        data = json.loads(request.POST["data"])
        token = data.get("token")
        business_id = data.get("business_id")
        quantity = data.get("quantity")
        
        usertoken = get_object_or_None(UserToken, token=token)
        if usertoken is None:
            return JsonResponse({
                "result": "error",
                "message": "token is null"
            })
            
        business = get_object_or_None(CyberCafe, business_id=business_id)
        if business is None:
            return JsonResponse({
                "result": "error",
                "message": "business is null"
            })
            
        user_cybercafe = get_object_or_None(UserCybercafes, user=usertoken.user, business=business)
        if user_cybercafe is None:
            return JsonResponse({
                "result": "error",
                "message": "user_cybercafe is null"
            })
            
        user_cybercafe.balance += quantity
        user_cybercafe.save()
        
        return JsonResponse({
            "result": "ok",
            "message": "balance has been added",except 
            "balance": user_cybercafe.balance
        })
        
    except Exception as e:
        return JsonResponse({
            "result": "error",
            "message": "something went wrong on the server",
            "traceback": str(e)
        })

