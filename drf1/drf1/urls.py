
from django.contrib import admin
from django.urls import path
from apiapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',views.student_detail),
    path('apicreate/',views.student_create),
]
