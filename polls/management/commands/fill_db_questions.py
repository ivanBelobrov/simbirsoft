from django.core.management import BaseCommand
from polls.models import Quiz, Choice, Question

QUESTIONS = [{
        'text': 'Как получить данные от пользователя',
        'quiz': Quiz.objects.get(uuid='1'),
        'uuid': '1-1',
        'choices': Choice.objects.filter(uuid__startswith='1-1-')
    },
    {
        'text': 'Какая библиотека отвечает за время',
        'quiz': Quiz.objects.get(uuid='1'),
        'uuid': '1-2',
        'choices': Choice.objects.filter(uuid__startswith='1-2-')
    },
    {
        'text': 'Сколько библиотек можно импортировать в один проект',
        'quiz': Quiz.objects.get(uuid='1'),
        'uuid': '1-3',
        'choices': Choice.objects.filter(uuid__startswith='1-3-')
    },
    {
        'text': 'Какие существуют типы переменных (выбери несколько вариантов)',
        'quiz': Quiz.objects.get(uuid='1'),
        'uuid': '1-4',
        'choices': Choice.objects.filter(uuid__startswith='1-4-')
    },
    {
        'text': 'Выберите неизменяемые типы данных '
                '(выбери несколько вариантов)',
        'quiz': Quiz.objects.get(uuid='1'),
        'uuid': '1-5',
        'choices': Choice.objects.filter(uuid__startswith='1-5-')
    }]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for question in QUESTIONS:
            new_question = Question.objects.create(uuid=question['uuid'],
                                                   text=question['text'],
                                                   quiz=question['quiz'])
            new_question.choices.set(question['choices'])
        return 'OK'
