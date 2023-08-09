from django.shortcuts import render
from django.shortcuts import HttpResponse
from loginpage_main.models import Home
from rest_framework.response import Response
from django.template import loader
from .serializers import Home_get_serializer, Home_post_serializer, Home_put_serializer
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
def home(request):
    display = "<h1>Welcome to the home page.</h1>"
    return HttpResponse(display)

# def get_user_details(self,request):
#     # details = ("First Name {}""Last Name {}""Email {}""Phone number {%d}""Address {}").format(Home.first_name, Home.last_name, Home.email, Home.phone_num, Home.address)
#     # template = loader.get_template("loginpage_main/user.html")
#     context = {"User ": Home.objects.get(id=3)}

#     return render(request,"loginpage_main/user.html",{"user":context})

# def put_and_post_user(request):
#     # context = {"Users ": Home.put}
#     return render(request,"loginpage_main/put_post_user.html",{}) 
@api_view(['GET'])
def get_user_details(request):
    details = Home.objects.all()
    serializer = Home_get_serializer(details,many=True)
    return Response(serializer.data)
    

@api_view(['POST'])
def post(request):
    serializer = Home_post_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
@api_view(['PUT'])
def put_details( request, **validated_data):
    serializer = Home_put_serializer(data=request.data, **validated_data, )
    if serializer.is_valid():
        serializer.update()
        serializer.save()
    return Response(serializer.data)