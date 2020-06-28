import csv

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from datetime import date
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

@login_required
def list_log(request):
    posts = Logs.objects.filter(datum__lte=date.today()).order_by('datum')
    return render(request, 'log/list_log.html', {'posts': posts})

def csv_export(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Eingetragen', 'Datum', 'Name', 'Vorname', 'Ziel', 'Grund', 'Von', 'Bis', 'Kostenstelle', 'Projekt'])

    for log in Logs.objects.all().values_list('timestamp', 'datum', 'name', 'vorname', 'ziel', 'grund', 'von', 'bis', 'kostenstelle', 'projekt'):
        writer.writerow(log)

    response['Content-Disposition'] = 'attachment; filename="Ausgangsbuch.csv"'

    return response

