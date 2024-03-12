from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Conference, ConferenceRegistration, MemberProfile
from .forms import ConferenceRegistrationForm, MemberProfileUpdateForm 

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
#----------  My CPDs Views --------------------------
@login_required
def my_cpds(request):
    context = {}
    return render(request, 'membership/my_cpds.html', context)




# ----------- User Update Views -------------------
@login_required
def profile_update(request):
    if request.method == 'POST':
        form = MemberProfileUpdateForm(request.POST, request.FILES, instance=request.user.memberprofile)
        if form.is_valid():
            form.save()
            return redirect('profile_update_success')
    else:
        form = MemberProfileUpdateForm(instance=request.user.memberprofile)
    context = {'form': form}
    return render(request,'membership/update_profile.html', context)


@login_required
def profile_update_success(request):
    return render(request,'membership/profile_update_success.html')

# ----------- Download Certificate Views -------------------
@login_required
def view_certs(request):
    return render(request,'membership/my_certs.html')