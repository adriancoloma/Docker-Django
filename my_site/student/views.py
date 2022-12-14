from django.shortcuts import render

# Create your views here.

#Import the Student model
from .models import Student
from .serializer import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


#Create and endpoint to get all students
class StudentList(APIView):
    def get(self, request):
        #Get all the students from the database
        students = Student.objects.all()
        #Serialize the data for the response
        serializer = StudentSerializer(students, many=True)
        #Return the serialized data
        return Response(serializer.data)

    def post(self):
        pass