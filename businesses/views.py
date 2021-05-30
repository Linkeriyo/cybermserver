from businesses.models import CyberCafe
from annoying.functions import get_object_or_None
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def check_business(request):
    try:
        business_id = request.POST["business_id"]
        business = get_object_or_None(CyberCafe, business_id=business_id)
        
        if business is None:
            return JsonResponse({
                "result": "ok",
                "message": "that id didn't match any businesses"
            })
            
        return JsonResponse({
            "result": "ok",
            "business": business.json()
        })
        
    except Exception as e:
        return JsonResponse({
            "result": "error",
            "message": "something went wrong on the server",
            "traceback": str(e)
        })