# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, QuestionViewSet, AnswerViewSet, QuestionRatingViewSet, AnswerRatingViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'question-ratings', QuestionRatingViewSet)
router.register(r'answer-ratings', AnswerRatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
