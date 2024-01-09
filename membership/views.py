from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context = {'title': 'ELTAN - Home'}
    return render(request, 'membership/index.html', context)

@login_required
def dash(request):
    pass
