from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.first, name='first'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('homepage/', views.homepage, name='homepage'),
    path('minutes/', views.minutes, name='minutes')
]
