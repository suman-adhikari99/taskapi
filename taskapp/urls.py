from django.urls import  path
from .views import *
from rest_framework import routers, urlpatterns, views
router = routers.DefaultRouter()
router.register(r'Posts', TaskViewSet)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',register,name='register'),
    path('login/',Login.as_view(), name='login'),

]