from django.core.management.base import BaseCommand
from core.models import Category, Question


class Command(BaseCommand):
    help = 'Delete a category with all its associated questions and answers.'

    def add_arguments(self, parser):
        parser.add_argument('category_id', type=int, help='ID of the category to delete')

    def handle(self, *args, **options):
        category_id = options['category_id']

        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"Category with ID {category_id} does not exist"))
            return

        question_ids = category.question_set.values_list('pk', flat=True)

        # Delete answers related to questions
        Question.objects.filter(pk__in=question_ids).delete()

        # Delete the category
        category.delete()

        self.stdout.write(
            self.style.SUCCESS(f"Category with ID {category_id} and associated questions and answers has been deleted"))
