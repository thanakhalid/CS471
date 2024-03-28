from django.shortcuts import render
from .models import Poems 

# Create your views here.
def show_base(request):
    return render(request, 'base.html')
def home(request):
    return render(request,'home.html',{})
def signUp(request):
    return render(request,'Registration.html')
def signIn(request):
    return render(request,'Login.html')
def cpoems(request):
    return render(request,'cpoems.html')
def poems(request, poet_cat):
    poems = Poems.objects.filter(poet_cat=poet_cat)
    context = {'poems': poems}
    return render(request, 'poems.html', context)