from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Users
from users.serializers import UsersSerializer


# Create your views here.
@csrf_exempt
def user_list(request):
    """
    List all code users, or create a new user
    """
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse((request))
        serializer = UsersSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user(request, login_id, login_pw):
    """
    get User by login_id, confirm right pw
    """
    try:
        db_user = Users.objects.get(login_id=login_id)
    except Users.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UsersSerializer(db_user)
        return JsonResponse(serializer.data)
    elif request.method == 'POST':
        serializer = UsersSerializer(db_user)
        db_login_pw = serializer.data['login_pw']
        if login_pw == db_login_pw: # 로그인 성공:
            return JsonResponse(serializer.data, status=200)
        else:
            return HttpResponse(status=400)