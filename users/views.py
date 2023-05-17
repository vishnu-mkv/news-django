from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'profile.html')


@login_required
def account_update(request):
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileUpdateForm(request.POST,
                                  request.FILES,
                                  instance=request.user.profile)
        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, f'Acoount Updated')
            return redirect('profile')
    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'uform' : uform,
        'pform' : pform,
    }
    return render(request, 'userupdate.html', context)

