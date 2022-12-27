from django.shortcuts import render
from app.forms import *
# Create your views here.
def brock(request):
    form=TopicForms()
    d={'form':form}
    if request.method=='POST':
        form_data=TopicForms(request.POST)
        if form_data.is_valid():
            form_data.save()
    return render(request,'brock.html',d)


def naga(request):
    form=WebpageForms()
    d={'form':form}
    if request.method=='POST':
        form_data=WebpageForms(request.POST)
        if form_data.is_valid():
            form_data.save()
    
    return render(request,'naga.html',d)


def roman(request):
    form=AccessRecordsForms()
    d={'form':form}
    if request.method=='POST':
        form_data=AccessRecordsForms(request.POST)
        if form_data.is_valid():
            form_data.save()
    
    return render(request,'roman.html',d)


