import json
from users.models import UserToken
from annoying.functions import get_object_or_None
from businesses.models import CyberCafe
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from computers.models import Computer


# Create your views here.
@csrf_exempt
def get_computers_by_business_id(request):
    try:
        data = json.loads(request.POST["data"])
        token = data.get("token")
        business_id = data.get("business_id")
        
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
            
        computers = Computer.objects.filter(business=business)
        
        computer_list = []
        
        for c in computers:
            computer_list.append(c.json())
        
        return JsonResponse({
            "result": "ok",
            "message": "computers retrieved",
            "computer_list": computer_list
        })
        
    except Exception as e:
        return JsonResponse({
            "result": "error",
            "message": "something went wrong on the server",
            "traceback": str(e)
        })
    
