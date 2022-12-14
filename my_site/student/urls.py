from .views import StudentList
from django.urls import path

urlpatterns = [
    path('students/', StudentList.as_view()),
]