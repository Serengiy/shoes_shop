from django.shortcuts import render
from users.forms import UserRegistrationForm


def registration_view(request):
    form = UserRegistrationForm(request.POST)
    return render(request, 'users/registration.html', {'form': form})
