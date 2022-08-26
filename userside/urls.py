from django.urls import path
from .import views
from .views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('login/',MyTokenObtainPairView.as_view(),name='login'),
    path('register/',TokenRegisterView.as_view(),name='tokenregister'),

    path('refresh_token/',TokenRefreshView.as_view(),name='refresh_token')
   
    
]