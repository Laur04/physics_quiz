from django.core.management.base import BaseCommand
from .models import Answer

class Command(BaseCommand):
    def handle(self, *args, **options):
        Answer.objects.all().delete()
