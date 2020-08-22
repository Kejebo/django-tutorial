from django.contrib import admin
from django.urls import path
from . import views

app_name='app_persons'

urlpatterns = [
    path('',views.init, name='home'),    
    path('insert/',views.insert , name='insert'),    
    path('edit/<int:id>',views.update, name='edit'),    
    path('delete/<int:id>',views.delete, name='delete'),    

]
