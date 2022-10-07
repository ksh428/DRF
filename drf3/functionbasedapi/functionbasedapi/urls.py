
from django.contrib import admin
from django.urls import path
from apiapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apistudent/',views.StudentList.as_view()),
    # path('apistudent/',views.StudentCreate.as_view()),
    path('apistudent/<int:pk>',views.StudentRetrieve.as_view()),
]
