from django.contrib import admin
from django.urls import path,include
from EducatorApp import views
urlpatterns=[
    path('', views.add_Educator, name='home'),

    path('delete/<int:id>/', views.delete_data, name='delete'),
    path('<int:id>/', views.update_data, name='update'),
]
