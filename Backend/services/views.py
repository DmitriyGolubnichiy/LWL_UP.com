from django.shortcuts import render, HttpResponseRedirect
from .forms import ServiceForm
from .models import Service, Basket
from users.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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

def contacts(request):
    return render(request,'services/contacts.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            error = 'Форма была неверной'


    form = ServiceForm()

    data = {
        'form':form,
        'error':error
    }

    return render(request, 'services/create.html',data)
@login_required
def basket_add(request, service_id):
    service = Service.objects.get(id=service_id)
    baskets = Basket.objects.filter(user=request.user, service = service)
    if not baskets.exists():
        Basket.objects.create(user=request.user,service=service,quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
