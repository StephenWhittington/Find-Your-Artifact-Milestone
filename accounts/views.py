from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

def index(request):
    """Returns the index.html file"""
    return render(request, 'index.html')
    
def logout(request):
    """logs the user out"""
    auth.logout(request)
    messages.success(request, "you have successfully been loged out!")
    return redirect(reverse('index'))
