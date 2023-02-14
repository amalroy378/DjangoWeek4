from django.shortcuts import render,redirect
from .models import Actor,LatestUpdates
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def login(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(home)
        
        else:
            messages.info(request,"Invalid User")
            return redirect(login)
    else:
        return render(request,'login.html')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect(login)


@login_required(login_url='login')
def cards(request): 
    dict_card={
        'card':Actor.objects.all()
    }
    return render(request,'cards.html',dict_card)



@login_required(login_url='login')
def posts(request):
    dict_posts={
        'post':LatestUpdates.objects.all()
    }
    return render(request,'posts.html',dict_posts)



    


