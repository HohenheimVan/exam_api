from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from esheets.models import Test, Student, StudentTest, TestQuestion, StudentResponse, StudentAnswerPoints, \
    StudentTestGrade
from esheets.permissions import IsOwnerOrReadOnly, IsStudentOwnerOrReadOnly
from esheets.serializers import UserSerializer, TestSerializer, StudentTestSerializer, StudentAnswerPointsSerializer, \
    StudentTestGradeSerializer, StudentSerializer, TestQuestionSerializer, StudentResponseSerializer


class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StudentTestViewSet(ModelViewSet):
    queryset = StudentTest.objects.all()
    serializer_class = StudentTestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsStudentOwnerOrReadOnly)

    def get_student(self):
        student = Student.objects.get(owner=self.request.user)
        return student

    def perform_create(self, serializer):
        serializer.save(owner=self.get_student())


class TestQuestionViewSet(ModelViewSet):
    queryset = TestQuestion.objects.all()
    serializer_class = TestQuestionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser)


class StudentResponseViewSet(ModelViewSet):
    queryset = StudentResponse.objects.all()
    serializer_class = StudentResponseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsStudentOwnerOrReadOnly)

    def get_student(self):
        student = Student.objects.get(owner=self.request.user)
        print(student)
        return student

    def perform_create(self, serializer):
        serializer.save(owner=self.get_student())


class StudentAnswerPointsViewSet(ModelViewSet):
    queryset = StudentAnswerPoints.objects.all()
    serializer_class = StudentAnswerPointsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class StudentTestGradeViewSet(ModelViewSet):
    queryset = StudentTestGrade.objects.all()
    serializer_class = StudentTestGradeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
