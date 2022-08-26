from django.urls import path
from .import views
from .views import *


urlpatterns = [
    path('details/',Vechicle_Data.as_view(),name='details'),
    path('details/<int:pk>',Vechicle_Datas.as_view(),name='detailslist'),
  
   
    
]