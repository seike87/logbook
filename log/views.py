from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from datetime import date
import calendar
from calendar import HTMLCalendar
from .models import Logs
from .forms import LogForm

# Create your views here.

def add_log(request):
    submitted = False
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = LogForm()
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'log/add_log.html', {'form': form, 'submitted': submitted})

def list_log(request):
    posts = Logs.objects.filter(datum__lte=date.today()).order_by('datum')
    return render(request, 'log/list_log.html', {'posts': posts})
