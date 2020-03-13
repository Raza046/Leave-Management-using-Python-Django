from django.urls import include, path

from .views import classroom, students, teachers

urlpatterns = [
    path('', classroom.home, name='home'),

    path('students/', include(([

    ], 'classroom'), namespace='students')),

    path('teachers/', include(([


    ], 'classroom'), namespace='teachers')),
]
