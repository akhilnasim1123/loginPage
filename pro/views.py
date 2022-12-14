from django.shortcuts import render, HttpResponse
from .models import studentData, Teacher


# Create your views here.
def index(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

    return render(request, 'index.html')
