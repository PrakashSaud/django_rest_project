from .models import User, Teacher, Student
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


# class StudentSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Student
#         fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Student
        fields = ['name', 'grade', 'roll_no', 'owner']


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['name', 'subject', 'students', 'owner']
        