from django.urls import path
from .import views

app_name = 'kyokigo'

urlpatterns = [
    path('', views.index,name='index'),
]
