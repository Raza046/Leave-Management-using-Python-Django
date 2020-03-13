from django.contrib import admin
from classroom.models import ( Student,User,
    Teacher,TeachLeaveApp,StudentLeaveApp )

# Register your models here.

class TeachAdmin(admin.ModelAdmin):

    class Meta:
        model = Teacher

admin.site.register(Teacher,TeachAdmin)

class StudAdmin(admin.ModelAdmin):

    class Meta:
        model = Student

admin.site.register(Student,StudAdmin)

class StLeaveAppAdmin(admin.ModelAdmin):

    class Meta:
        model = StudentLeaveApp

admin.site.register(StudentLeaveApp,StLeaveAppAdmin)

class TeachLeaveAppAdmin(admin.ModelAdmin):

    class Meta:
        model = TeachLeaveApp

admin.site.register(TeachLeaveApp,TeachLeaveAppAdmin)


class UserAdmin(admin.ModelAdmin):

    class Meta:
        model = User

admin.site.register(User,UserAdmin)
