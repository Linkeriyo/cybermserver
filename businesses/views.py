from users.models import UserCybercafes, UserToken
from users.views import check_token
from businesses.models import CyberCafe, Post
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
    
@csrf_exempt
def get_businesses_by_user(request):
    try:
        token = request.POST["token"]
        
        usertoken = get_object_or_None(UserToken, token=token)
        if usertoken is None:
            return JsonResponse({
                "result": "error",
                "message": "token is null"
            })
        
        businesses = UserCybercafes.objects.filter(user=usertoken.user)
        
        business_list = []
        
        for b in businesses:
            business_list.append(b.business.json())
        
        return JsonResponse({
            "result": "ok",
            "message": "buinesses retrieved",
            "business_list": business_list
        })
        
    except Exception as e:
        return JsonResponse({
            "result": "error",
            "message": "something went wrong on the server",
            "traceback": str(e)
        })
    

@csrf_exempt
def get_posts_by_business(request):
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
        
        posts = Post.objects.filter(business=business)
        
        post_list = []
        
        for p in posts:
            post_list.append(p.post.json())
            
        return JsonResponse({
            "result": "ok",
            "message": "posts retreived",
            "post_list": post_list
        })
        
    except Exception as e:
        return JsonResponse({
            "result": "error",
            "message": "something went wrong on the server",
            "traceback": str(e)
        })