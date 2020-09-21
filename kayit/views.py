from django.shortcuts import render ,redirect
from .forms import KayitlarForm
import random
from .models import Kayitlar

def index(request):

    fotolar = list(Kayitlar.objects.values_list('Fotograf', flat=True))

    photo1 = random.sample(fotolar,1)
    print(photo1)
    photo2 = random.sample(fotolar,1)
    print(photo2)

    while photo1 == photo2:
        photo2 = random.sample(fotolar, 1)
    context = {'photo1':photo1,'photo2':photo2}
    return render(request, 'kayit/index.html',context)

def about(request):
    return render(request, 'kayit/about.html')

def kayit(request):
    if request.method == "POST":
        form = KayitlarForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = KayitlarForm()
    return render(request,"kayit/form.html",{"form":form})

