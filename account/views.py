from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm, MemberSignupForm
from django.contrib.auth import login as auth_login, logout
# Create your views here.


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
            
    else:
        form = CustomAuthenticationForm()
    return render(request, 'account/login.html', {
        'title': 'ELTAN', 
        'form': form
    })


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        member_form = MemberSignupForm(request.POST)

        if form.is_valid() and member_form.is_valid():
            user = form.save()
            member = member_form.save(commit=False)
            member.user = user
            member.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
        member_form = MemberSignupForm()

    return render(request, 'account/register.html', {
        'title': 'ELTAN', 
        'form': form,
        'member_form': member_form
    })

def logout_view(request):
    logout(request)
    return redirect('login')