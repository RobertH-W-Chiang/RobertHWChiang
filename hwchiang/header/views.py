import django
from django.shortcuts import render


def about(request):
    return render(request,
                  'about.html',
                  {'django_version': django.get_version()})