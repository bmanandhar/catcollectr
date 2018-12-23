from django.shortcuts import render 
from .models import Cat
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CatForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    cats = Cat.objects.all()
    form = CatForm()
    return render(request, 'index.html', {'cats':cats, 'form':form})

class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

cats = [
    Cat('Polo', 'tabby', 'foul little demon', 3),
    Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
    Cat('Raven', 'black tripod', '3 legged cat', 4)
]

def show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'show.html', {'cat': cat})

def post_cat(request):
    form = CatForm(request.POST)
    if form.is_valid:
        cat = form.save(commit = False)
        cat.user = request.user
        cat.save()
    return HttpResponseRedirect('/')

    if form.is_valid():
        cat = Cat(
            name=form.cleaned_data['name'],
            breed=form.cleaned_data['breed'],
            description=form.cleaned_data['description'],
            age=form.cleaned_data['age']
            )
        cat.save()
    return HttpResponseRedirect('/')

def index(request):
    cats = Cat.objects.all()
    form = CatForm()
    return render(request, 'index.html', {'cats':cats, 'form':form})

def profile(request, username):
    user = User.objects.get(username=username)
    cats = Cat.objects.all()
    return render(request, 'profile.html', {'username': username, 'cats': cats})

def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = aunthenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been desabled.")
            else:
                print("The username and/or password is incorrect.")
        else: 
            form = LoginForm()
            return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def like_cat(request):
    cat_id = request.GET.get('cat_id', None)

    likes = 0
    if (cat_id):
        cat = Cat.objects.get(id=int(cat_id))
        if cat is not None:
            likes += cat.likes
            cat.likes = likes 
            cat.save()
    return HttpResponse(likes)