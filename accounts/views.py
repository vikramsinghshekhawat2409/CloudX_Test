from django.shortcuts import render
from django.http import HttpResponse

from accounts.forms import UserForm,UserProfileInfoForm

from django.contrib.auth.models import User
# Create your views here.


def index(request):
    """
    :param request:
    :return: returns rendered html template with welcome message including an username if the user is logged in
             and if not so returns rendered html asking user to register or log in
             and if any exception raises returns an internal server error with the error
    """
    try:
        return render(request,'accounts/index.html')
    except Exception as e:
        return HttpResponse(e, status=500)


def signup(request):
    """
    performs registration of the user through forms
    :param request: includes user attributes from user form i.e first_name, last_name, email, password
    :return: returns the success if the user is registered successfully and forms is valid else returns to the user form
    """
    try:
        registered = False
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)
            user_form.username = request.POST['email']
            profile_form = UserProfileInfoForm(data=request.POST)
            if user_form.is_valid() and profile_form.is_valid():
                user = User()
                user.first_name = request.POST.get('first_name')
                user.last_name = request.POST.get('last_name')
                user.email = request.POST.get('email')
                user.username = request.POST.get('email')
                user.set_password(request.POST.get('password'))
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                registered = True
            else:
                print(user_form.errors,profile_form.errors)
        else:
            user_form = UserForm()
            profile_form = UserProfileInfoForm()
        return render(request,'accounts/registration.html',
                              {'user_form':user_form,
                               'profile_form':profile_form,
                               'registered':registered})
    except Exception as e:
        return HttpResponse(e, status=500)
