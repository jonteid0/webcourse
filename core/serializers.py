from rest_framework import serializers
from .models import Category, Question, Answer, QuestionRating, AnswerRating

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class QuestionRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionRating
        fields = '__all__'

class AnswerRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerRating
        fields = '__all__'
