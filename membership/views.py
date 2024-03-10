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
    user = request.user
    context = {
        'title': 'ELTAN - Dashboard',
        'user': user,
        }
    return render(request,'membership/dash.html', context)


@login_required
def my_conferences(request, user_id):
    context = {'title': 'ELTAN - My Conferences'}
    return render(request,'membership/my_conferences.html', context)


@login_required
def my_cpds(request):
    context = {}
    return render(request, 'membership/my_cpds.html', context)
