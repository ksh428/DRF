
from django.contrib import admin
from django.urls import path
from crudapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/getstudent/',views.get_student),
    path('api/poststudent/',views.student_create),
    path('api/updatestudent/',views.student_update),
]
