from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Creating views.
def register(request):
    form = UserCreationForm()
    return render (request. 'user/register.html', {'form':form})

