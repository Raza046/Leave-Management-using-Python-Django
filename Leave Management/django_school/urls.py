from django.urls import include, path
from django.contrib import admin
from classroom.views import classroom, students, teachers,Myadmin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('classroom.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('accounts/signup/admin/', Myadmin.AdminSignUpView.as_view(), name='admin_signup'),
    path('students',students.Stpage ,name='students'),
    path('teachers',teachers.Tpage ,name='teachers'),
    path('logout',classroom.Logout ,name='logout'),
    path('sleaveApp',students.StLeaveApp,name='sleaveApp'),
    path('Showapp',teachers.ShowApp,name='Showapp'),
    path('tleaveApp',teachers.TLeaveApp,name='tleaveApp'),
    path('ShowTResp',students.StatusOfApp,name='ShowTResp'),
    path('adminpage',Myadmin.Adpage ,name='adminpage'),
    path('ShowTapp',Myadmin.ShowTeacherApp ,name='ShowTapp'),
    path('TAppStatus',teachers.TeacherStatusOfApp,name='TAppStatus'),


]
