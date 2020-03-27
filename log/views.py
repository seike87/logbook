from django.shortcuts import render

# Create your views here.

def add_log(request):
    return render(request, 'log/add_log.html', {})
