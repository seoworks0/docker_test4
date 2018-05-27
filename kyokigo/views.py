from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import Kyokigo_Form
from .kyokigo import kyoki
from django.http import HttpResponse
import datetime
import csv
from django.contrib.auth.mixins import LoginRequiredMixin



def index(request):
    form = Kyokigo_Form(request.POST or None)
    result = []
    kyokigo_n = []
    kyokigo_v = []

    if request.method == 'POST' and form.is_valid():
        form.save()
        keyword = request.POST['text']
        kyokigo_v,kyokigo_n = kyoki(keyword)
        print(len(kyokigo_n[0]))
        #kyokigo_n=[['/,', ', ログイン, ログイン, http://musmus.main.jp/, http:', 'https://www.youtube.com/watch?v=kzkSnSGBlEk'], ['保護', '終了いたしました。ご了承ください。, , , , 会社概要, 個人情報保護への取り組み', 'https://unkokanji.com/survey']]
        #kyokigo_v=[['/,', ', ログイン, ログイン, http://musmus.main.jp/, http:', 'https://www.youtube.com/watch?v=kzkSnSGBlEk'], ['保護', '終了いたしました。ご了承ください。, , , , 会社概要, 個人情報保護への取り組み', 'https://unkokanji.com/survey']]
        #result = [kyokigo_n,kyoukigo_v]
        #result = [["keyword","2018/03/14","10","https://to-kei.net"]]


        return render(request, 'kyokigo/result.html',{'noun': kyokigo_n,'verb':kyokigo_v,})

    context = {
        'form':form,
    }
    return render(request, 'kyokigo/form.html',context)
