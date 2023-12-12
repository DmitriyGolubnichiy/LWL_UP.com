from django.shortcuts import render, redirect
from .forms import ServiceForm
from .models import Service

def index(request):
    context = {'title': "LWL_UP.com",}

    return render(request, "services/index.html", context)

def training_programs(request):
    context = {'title': "Training_Programs",
               'services': Service.objects.all(),
               }
    return render(request, 'services/training_programs.html',context)

def me(request):
    return render(request,'services/me.html')

def test_and_exercises(request):
    return  render(request,'services/test_and_exercises.html')

def log_in(request):
    return render(request, 'services/log_in.html')

def contacts(request):
    return render(request,'services/contacts.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_programs')
        else:
            error = 'Форма была неверной'


    form = ServiceForm()

    data = {
        'form':form,
        'error':error
    }

    return render(request, 'services/create.html',data)