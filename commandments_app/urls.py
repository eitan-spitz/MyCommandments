from django.urls import path
from commandments_app import views

app_name = 'commandments_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('all_commandments/', views.all_commandments, name='all_commandments'),
    path('commandments_filtering/', views.CommandmentsFiltering.as_view(), name='commandments_filtering'),
    path('mitzvah/<int:pk>', views.MitzvahPage.as_view(), name='mitzvah_details'),
]