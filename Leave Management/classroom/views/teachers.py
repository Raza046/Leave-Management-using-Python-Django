from django.forms.formsets import formset_factory
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..decorators import teacher_required
from ..forms import TeachLeaveAppForm,TeacherSignUpForm,TeachLeaveAppForm,AppStatusForm
from ..models import  User,Teacher,StudentLeaveApp,Student,TeachLeaveApp


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('teachers')

#def TeachLeaveApp(request):

#    form = StdLeaveAppForm(request.POST)

 #   if form.is_valid():
  #      form.save()

  #  context = {'form':form}

   # return render(request,'stApp.html',context)


def ShowApp(request): # It will show all application send from students
    
    teacher = Teacher.objects.filter(user=request.user).first()
    app = StudentLeaveApp.objects.filter(to_teacher = teacher).all()
    app1 = StudentLeaveApp.objects.filter(to_teacher = teacher).all()
    
    app2 = StudentLeaveApp.objects.filter(id=request.POST.get('answer')).all()

    for items in app2:

        items.status = request.POST.get('status')
        items.save()

    context = { 'app':app }

    return render(request,'ShowApp.html',context)


def Tpage(request):

    context = locals()

    return render(request,'tpage.html',context)


def TLeaveApp(request):

    form = TeachLeaveAppForm(request.POST)
    teacher = Teacher.objects.filter(user=request.user).first()

    if form.is_valid():
        form.instance.user = teacher
        form.save()

    context = {'form':form}

    return render(request,'tApp.html',context)


def TeacherStatusOfApp(request):

    teacher = Teacher.objects.filter(user=request.user).first()

    app = TeachLeaveApp.objects.filter(user=teacher).all()

    context = { 'app':app }

    return render(request,'TeacherAppStatus.html',context)


