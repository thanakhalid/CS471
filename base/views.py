from django.shortcuts import render

# Create your views here.
def show_base(request):
    return render(request, 'base.html')
def home(request):
    return render(request,'home.html',{})
def signUp(request):
    return render(request,'Registration.html')
def signIn(request):
    return render(request,'Login.html')