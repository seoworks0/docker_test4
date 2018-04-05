from django.urls import path
from .import views

app_name = 'suggestnet'

urlpatterns = [
    path('', views.index,name='index'),
]
