from django.shortcuts import render,redirect
from shopapp.models import Buyer
from shopapp.forms import BuyerForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import login,logout
from django.http import HttpResponse

#from django.contrib.auth.forms import UserCreationForm
#def home(request):
    #form = UserCreationForm()
    #return render(request, 'index.html', {'form' : form})

# Create your views here.

def buyer(request):
    buyerform = BuyerForm()
    if request.method == "POST":
        form = BuyerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/buyer/list')

    return render(request, 'buyer.html',{'buyer': buyerform})

def index(request):
    return render(request, 'index.html')


def loginuser(request):
    # if request.method == "POST":
    loginform = UserForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    return render(request, 'login.html',{'loginForm': loginform})
def user_logout(request):
    logout(request)
    return redirect('/')