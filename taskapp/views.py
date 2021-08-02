from rest_framework.generics import GenericAPIView
from taskapp.models import Register
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout,login
#from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm

import jwt,json
from rest_framework import serializers, views
from rest_framework.response import Response
from django.contrib.auth.models import User
# Create your views here.




#pip install PyJWT
def register(request):
    if request.method=='POST':
        firstname=request.POST.get['FirstName']
        lastname=request.POST.get['LastName']
        email = request.POST.get['Email']
        password = request.POST.get['Password']
        register=Register.objects.create(FirstName=firstname,LastName=lastname,Email=email,Password=password)
        user = User.objects.create_user(username= email,email= email,password= password)    
        user.save()
        return HttpResponse("registered")
    else:
        form= RegisterForm()
    return render(request,'registration.html', {'form':form})

class Login(views.APIView):

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")
        
        email = request.data['username']
        password = request.data['password']
        user=authenticate(request, username=email, password=password)
        
        
        print(email)
        print(password)
        try:
            user = User.objects.get(username=email)
            print(user)
        except User.DoesNotExist:
            return Response({'Error': "Invalid username/password"}, status="400")
        if user:
            
            payload = {
                'id': user.id,
                'email': user.email,
            }
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}

            return HttpResponse(
              json.dumps(jwt_token),
              status=200,
              content_type="application/json",
              
            )
            login(emial, password)
        else:
            return Response(
              json.dumps({'Error': "Invalid credentials"}),
              status=400,
              content_type="application/json"
            )


from .models import Task
from .serializer import TaskSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


