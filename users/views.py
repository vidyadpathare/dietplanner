from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserProfileForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            # profile auto-created by signals
            profile = user.userprofile
            profile.age = profile_form.cleaned_data['age']
            profile.gender = profile_form.cleaned_data['gender']
            profile.weight = profile_form.cleaned_data['weight']
            profile.height = profile_form.cleaned_data['height']
            profile.goal = profile_form.cleaned_data['goal']
            profile.save()
            login(request, user)
            return redirect('meals:dashboard')   # ✅ FIXED
    else:
        form = SignUpForm()
        profile_form = UserProfileForm()
    return render(request, 'users/signup.html', {'form': form, 'profile_form': profile_form})

@login_required
def edit_profile(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('meals:dashboard')   # ✅ FIXED
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'users/profile_form.html', {'form': form})
