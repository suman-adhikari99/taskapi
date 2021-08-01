from taskapp.models import Register
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
#from django.contrib.auth import authenticate, logout
#from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm

import jwt,json
from rest_framework import views
from rest_framework.response import Response
from django.contrib.auth.models import User
# Create your views here.




#pip install PyJWT
def register(request):
    if request.method=='POST':
        firstname=request.POST['FirstName']
        lastname=request.POST['LastName']
        email = request.POST['Email']
        password = request.POST['Password']
        #print(firstname)
        register=Register.objects.create(FirstName=firstname,LastName=lastname,Email=email,Password=password)
        user = User.objects.create_user( email,email= email,password= password)
        #user.firstname=firstname
        user.lastname=lastname
        user.save()
        return HttpResponse("registered")
    else:
        form= RegisterForm()
    return render(request,'registration.html', {'form':form})

class Login(views.APIView):

    def post(self, request, *args, **kwargs):
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")
        
        username = request.data['email']
        password = request.data['password']
        print(username)
        print(password)
        try:
            user = User.objects.get(username=username, password=password)
            print(user.email)
            print(user.id)
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
              content_type="application/json"
            )
        else:
            return Response(
              json.dumps({'Error': "Invalid credentials"}),
              status=400,
              content_type="application/json"
            )

    def get(self, request):
        
        return render(request, 'login.html')
