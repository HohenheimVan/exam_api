from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from esheets.views import TestViewSet, StudentTestViewSet, UserViewSet, TestQuestionViewSet, \
    StudentAnswerPointsViewSet, StudentTestGradeViewSet, StudentViewSet, StudentResponseViewSet

router = DefaultRouter()
router.register(r'test', TestViewSet)
router.register(r'student', StudentViewSet)
router.register(r'student-test', StudentTestViewSet)
router.register(r'test-question', TestQuestionViewSet)
router.register(r'student-response', StudentResponseViewSet)
router.register(r'student-answer-points', StudentAnswerPointsViewSet)
router.register(r'student-test-grade', StudentTestGradeViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'', include(router.urls)),
]
