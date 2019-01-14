from django.contrib.auth.models import User
from rest_framework import serializers
from esheets.models import Test, Student, StudentTest, TestQuestion, StudentResponse, StudentAnswerPoints, \
    StudentTestGrade


class TestSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    questions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Test
        fields = ('id', 'test_name', 'owner', 'questions')


class StudentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Student
        fields = ('id', 'owner', 'name')


class StudentTestSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.name')
    student_response = serializers.StringRelatedField(many=True)

    class Meta:
        model = StudentTest
        fields = ('id', 'owner', 'test', 'student_response')


class TestQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestQuestion
        fields = ('id', 'test', 'question')


class StudentResponseSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = StudentResponse
        fields = ('id', 'owner', 'student_test', 'question', 'answer')


class StudentAnswerPointsSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentAnswerPoints
        fields = ('id', 'student_response', 'points')


class StudentTestGradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentTestGrade
        fields = ('id', 'grade', 'student_test')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')
