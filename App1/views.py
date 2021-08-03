from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def home(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'App1/home.html', context)


def clicked(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.clicks += 1
        user.save()
        return redirect('home')
    context = {
        'name': user.name,
        'clicks': user.clicks
    }
    return render(request, 'App1/second_page.html', context)