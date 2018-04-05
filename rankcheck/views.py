from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import Plus1_Form
from .juni import main
from django.http import HttpResponse
import datetime
import csv
from django.contrib.auth.mixins import LoginRequiredMixin



def index(request):
    form = Plus1_Form(request.POST or None)
    result = []

    if request.method == 'POST' and form.is_valid():
        form.save()
        keyword = request.POST['text']
        ownurl = request.POST['ownurl']
        #result = [["keyword","2018/03/14","10","https://to-kei.net"]]

        for i,key in enumerate(keyword.split("\n")):
            rank,r_url=main(key,ownurl)
            date = datetime.date.today().strftime('%x')
            result1 = [key,date,rank,r_url]
            print(result1)
            result += [result1]
        #print(ownurl)


        return render(request, 'rankcheck/result.html',{'ranks': result,})

    context = {
        'form':form,
    }
    return render(request, 'rankcheck/form.html',context)
