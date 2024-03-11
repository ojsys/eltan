from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Conference, ConferenceRegistration
from .forms import ConferenceRegistrationForm

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

# Here we wrote the logic for all conference related components
@login_required
def my_conferences(request, user_id):
    conferences = Conference.objects.all()
    context = {
        'title': 'ELTAN - My Conferences',
        'conferences': conferences,
               }
    return render(request,'membership/my_conferences.html', context)

@login_required
def conference_registration(request, conference_id):
    form = ConferenceRegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        conference_id = form.cleaned_data['conference'].id
        conference = Conference.objects.get(pk=conference_id)
        ConferenceRegistration.objects.create(user=request.user, conference=conference)
        return redirect('user_conferences')
    
    context = {'form':form}
    return render(request,'membership/conference_registration.html', context)


@login_required
def register_for_conference(request, conference_id):
    conference = Conference.objects.get(pk=conference_id)
    ConferenceRegistration.objects.create(user=request.user, conference=conference)
    return redirect('my_conf')

@login_required
def user_conferences(request):
    conferences = Conference.objects.all()
    user_conferences = ConferenceRegistration.objects.filter(user=request.user)
    return render(request, 'membership/my_conferences.html', {'user_conferences': user_conferences, 'conferences': conferences})

#-------- End of conference components ------------------------

@login_required
def my_cpds(request):
    context = {}
    return render(request, 'membership/my_cpds.html', context)
