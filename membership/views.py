from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context = {'title': 'ELTAN - Home'}
    return render(request, 'membership/index.html', context)

def about(request):
    context = {'title': 'ELTAN - About'}
    return render(request,'membership/about.html', context)


def sigs(request):
    context = {'title': 'ELTAN - SIGs'}
    return render(request, 'membership/sigs.html', context)


@login_required
def dash(request):
    pass
