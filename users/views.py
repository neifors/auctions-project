from django.shortcuts import render, redirect
from .forms import UserSignupForm

def signup(req):
    if req.method == 'POST':
        form = UserSignupForm(req.POST)
        if form.is_valid():
            form.save()
            # req.session['email'] = form.cleaned_data.get('email')
            return redirect('login')
    else:
        form = UserSignupForm()
    data = {'form': form}
    return render(req, "users/signup.html", data)
