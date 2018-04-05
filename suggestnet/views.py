from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import Suggest_Form
from django.http import HttpResponse
import datetime
import csv
from django.contrib.auth.mixins import LoginRequiredMixin
from .suggest import main



def index(request):
    form = Suggest_Form(request.POST or None)
    result = []

    if request.method == 'POST' and form.is_valid():
        form.save()
        keyword = request.POST['text']
        main(keyword)
        result = [["keyword","2018/03/14","10","https://to-kei.net"]]


        return render(request, 'suggestnet/result.html')

    context = {
        'form':form,
    }
    return render(request, 'suggestnet/form.html',context)
