from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def index(request):
    user_list = User.objects.order_by('-id')[:5]
    context = {'user_list': user_list} 
    return render(request, 'users/index.html', context)