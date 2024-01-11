from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from services.models import Basket

from django.contrib.auth.decorators import login_required


from users.forms import (UserLoginForm, UserRegistrationForm, UserProfileForm)

def log_in(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()
    context = {'form':form}
    return render(request, 'users/log_in.html',context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Вы успешно зарегистрированы!')
            return HttpResponseRedirect(reverse('users:log_in'))
    else:
        form = UserRegistrationForm()
    context = {'form':form}
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user ,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)

    total_sum = sum(basket.sum() for basket in baskets)

    context = {'title':'Профиль',
               'form':form,
               'baskets': baskets,
               'total_sum' : total_sum,

               }
    return render(request,'users/profile.html',context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))