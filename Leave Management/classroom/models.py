from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    student = models.ForeignKey(Student,on_delete='CASCADE', null=True)

    def __str__(self):
        return self.user.username

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    teacher = models.ForeignKey(Teacher,on_delete='CASCADE', null=True)

    def __str__(self):
        return self.user.username
   

class StudentLeaveApp(models.Model):

    user = models.ForeignKey(Student,on_delete='CASCADE')
    to_teacher = models.ForeignKey(Teacher,on_delete='CASCADE')
    content = models.CharField(max_length=1000)
    status = models.CharField(max_length=100,null=True)


class AppStatus(models.Model):

    leaveApp = models.ForeignKey(StudentLeaveApp,on_delete='CASCADE')
    status = models.CharField(max_length=100,null=True)


class TeachLeaveApp(models.Model):

    user = models.ForeignKey(Teacher,on_delete='CASCADE')
    to_admin = models.ForeignKey(Admin,on_delete='CASCADE')
    content = models.CharField(max_length=1000)
    status = models.CharField(max_length=100,null=True)

