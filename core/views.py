from django.db.models import Q
from django.shortcuts import render, get_object_or_404 , redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Question, Answer, QuestionRating, AnswerRating
from .forms import QuestionForm , AnswerForm
from .pagination import QuestionPagination
from .serializers import CategorySerializer, QuestionSerializer, AnswerSerializer, QuestionRatingSerializer, \
    AnswerRatingSerializer


def home(request):
    questions = Question.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'home.html', {'questions': questions ,'categories': categories, 'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def question_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    questions = category.question_set.all()
    return render(request, 'question_list.html', {'category': category, 'questions': questions})

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect('question_detail', question_id=question_id)
    else:
        form = AnswerForm()
    return render(request, 'question_detail.html', {'question': question, 'form': form})



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = QuestionPagination

    @action(methods=['GET'], detail=False)
    def filter_question(self, request):
        category_name = request.query_params.get('category_id', '')
        keyword = request.query_params.get('keyword', '')

        filter_conditions = Q()

        if category_name:
            filter_conditions &= Q(category__id=category_name)
        if keyword:
            filter_conditions &= (Q(title__icontains=keyword) | Q(content__icontains=keyword))

        filtered_questions = Question.objects.filter(filter_conditions)

        serializer = QuestionSerializer(filtered_questions, many=True)
        return Response(serializer.data)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['question']


class QuestionRatingViewSet(viewsets.ModelViewSet):
    queryset = QuestionRating.objects.all()
    serializer_class = QuestionRatingSerializer

class AnswerRatingViewSet(viewsets.ModelViewSet):
    queryset = AnswerRating.objects.all()
    serializer_class = AnswerRatingSerializer
