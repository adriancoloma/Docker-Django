from django.shortcuts import render

# Create your views here.

#Import the Student model
from .models import Student
from .serializer import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

#import status
from rest_framework import status
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

class AddStudent(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            print("entra")
            serializer.save()
            print("salio")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)