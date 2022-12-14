from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    #Create a field for the student's name
    name = serializers.CharField(max_length=50)
    #Create a field for the student's age
    age = serializers.IntegerField()
    #Create a field for the student's email
    email = serializers.EmailField()