from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.models import User,auth


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teachers')
        elif request.user.is_student:
            return redirect('students')
        elif request.user.is_superuser:
            return redirect('adminpage')

    return render(request, 'classroom/home.html')

def Logout(request):

    auth.logout(request)
    return render(request, 'classroom/home.html')
