from django.test import TestCase
from django.urls import reverse
from .models import Question, Answer


class QuestionAnswerTests(TestCase):
    def setUp(self):
        self.question = Question.objects.create(title='Test Question', content='This is a test question.')

    def test_question_detail_view(self):
        response = self.client.get(reverse('question_detail', args=[self.question.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.question.title)
        self.assertContains(response, self.question.content)

    def test_add_answer(self):
        response = self.client.post(reverse('question_detail', args=[self.question.id]), {'content': 'Test Answer'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.question.answer_set.count(), 1)
        answer = self.question.answer_set.first()
        self.assertEqual(answer.content, 'Test Answer')

    def test_question_ratings(self):
        response = self.client.post(reverse('question_rating', args=[self.question.id]), {'rating': 4})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.question.question_rating.count(), 1)
        rating = self.question.question_rating.first()
        self.assertEqual(rating.rating, 4)

    def test_answer_ratings(self):
        answer = Answer.objects.create(question=self.question, content='Test Answer')
        response = self.client.post(reverse('answer_rating', args=[answer.id]), {'rating': 3})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(answer.answer_rating.count(), 1)
        rating = answer.answer_rating.first()
        self.assertEqual(rating.rating, 3)

