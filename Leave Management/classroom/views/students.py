from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count, Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from django.views import View

from ..decorators import student_required
from ..forms import StdLeaveAppForm,StudentSignUpForm
from ..models import Teacher,Student, User , TeachLeaveApp, StudentLeaveApp


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('students')

def StLeaveApp(request):

    form = StdLeaveAppForm(request.POST)
    
    student = Student.objects.filter(user=request.user).first()

    if form.is_valid():
        form.instance.user=student
        form.save()

    context = {'form':form}

    return render(request,'stApp.html',context)

def StatusOfApp(request):

    student = Student.objects.filter(user=request.user).first()

    app = StudentLeaveApp.objects.filter(user=student).all()

    context = { 'app':app }

    return render(request,'AppStatus.html',context)


def Stpage(request):

    student = Student.objects.filter(user=request.user).first()

    app = StudentLeaveApp.objects.filter(user=student).all()

    context = { 'app':app }

    return render(request,'stpage.html',context)
