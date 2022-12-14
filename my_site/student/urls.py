from .views import StudentList, AddStudent
from django.urls import path

urlpatterns = [
    path('students/', StudentList.as_view()),
    path('add/', AddStudent.as_view()),
]