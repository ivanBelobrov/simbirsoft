from django.core.management import BaseCommand
from polls.models import Quiz

QUIZ = {
        'title': '"Тест на знание языка Python"',
        'uuid': '1'
    }


class Command(BaseCommand):
    def handle(self, *args, **options):
        Quiz.objects.create(uuid=QUIZ['uuid'],
                            title=QUIZ['title'])
        return 'OK'
