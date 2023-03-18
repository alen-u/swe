from django.urls import path,include
from django.views.generic import TemplateView
from .views import *
urlpatterns = [
    path('', login_view , name='login'),
    path('logout', citizen_logout , name='login'),
    path('register', register_view , name='login'),
    path('dashboard/', dashboard , name='dashboard'),
    path('create_case/', create_case , name='create_case'),
	path('user_case_detail/<int:id>/', user_case_detail , name='user_case_detail'),
]
