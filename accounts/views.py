from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect



# Create your views here.
def render_dashboard(request):
    return render(request, 'dashboard_layout.html')

@login_required(login_url='/accounts/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'You have successfully changed the password')
            return redirect('profile')
        else:
            messages.error(request, 'Error in changing password')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {
        'form': form
    })



def render_404(request, exception):
    return render(request, 'accounts/error-404.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
               return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')