from django.shortcuts import render
from firstapp import forms
from firstapp import models

def formview(request):
    formdata=forms.formtable()
    if request.method=='POST':
        form=forms.formtable(request.POST)
        if form.is_valid():
            form.save()
            info=models.modeltable.objects.last()
            return render(request,"htmlpage.html",{"displaying":info})

    return render(request,"formhtml.html",{"display":formdata})
