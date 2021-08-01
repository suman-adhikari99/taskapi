from django.urls import  path
#from . import views
from .views import *
#from rest_framework import routers, urlpatterns, views
#
#router = routers.DefaultRouter()
##router.register(r'Posts', PostViewSet)
##router.register(r'article',ArticleViewSet)
#
#
#
#
#from rest_framework_simplejwt.views import (
#    TokenObtainPairView,
#    TokenRefreshView,
#    TokenVerifyView,
#)


urlpatterns = [
    #path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',register,name='register'),
    path('login/',Login.as_view(), name='login'),

]