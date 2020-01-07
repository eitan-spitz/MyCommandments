from django.urls import path
from commandments_app import views

app_name = 'commandments_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage')
]