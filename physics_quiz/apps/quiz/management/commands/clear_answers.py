from django.core.management.base import BaseCommand
from physics_quiz.apps.quiz.models import Answer

class Command(BaseCommand):
    def handle(self, *args, **options):
        Answer.objects.all().delete()
