from django.core.management import BaseCommand
from polls.models import Choice

CHOICES = [{
        'text': 'get()',
        'is_correct': False,
        'uuid': '1-1-1'
    },
    {
        'text': 'input()',
        'is_correct': True,
        'uuid': '1-1-2'
    },
    {
        'text': 'readline()',
        'is_correct': False,
        'uuid': '1-1-3'
    },
    {
        'text': 'cin()',
        'is_correct': False,
        'uuid': '1-1-4'
    },
    {
        'text': 'time',
        'is_correct': True,
        'uuid': '1-2-1'
    },
    {
        'text': 'localtime',
        'is_correct': False,
        'uuid': '1-2-2'
    },
    {
        'text': 'clock',
        'is_correct': False,
        'uuid': '1-2-3'
    },
    {
        'text': 'Time',
        'is_correct': False,
        'uuid': '1-2-4'
    },
    {
        'text': 'неограниченное количество',
        'is_correct': True,
        'uuid': '1-3-1'
    },
    {
        'text': 'не более 10',
        'is_correct': False,
        'uuid': '1-3-2'
    },
    {
        'text': 'не более 5',
        'is_correct': False,
        'uuid': '1-3-3'
    },
    {
        'text': 'не более 23',
        'is_correct': False,
        'uuid': '1-3-4'
    },
    {
        'text': 'var',
        'is_correct': False,
        'uuid': '1-4-1'
    },
    {
        'text': 'dec',
        'is_correct': False,
        'uuid': '1-4-2'
    },
    {
        'text': 'float',
        'is_correct': True,
        'uuid': '1-4-3'
    },
    {
        'text': 'bool',
        'is_correct': True,
        'uuid': '1-4-4'
    },
    {
        'text': 'dict',
        'is_correct': True,
        'uuid': '1-5-1'
    },
    {
        'text': 'int',
        'is_correct': False,
        'uuid': '1-5-2'
    },
    {
        'text': 'set',
        'is_correct': True,
        'uuid': '1-5-3'
    },
    {
        'text': 'str',
        'is_correct': False,
        'uuid': '1-5-4'
    }]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for choice in CHOICES:
            Choice.objects.create(uuid=choice['uuid'],
                                  text=choice['text'],
                                  is_correct=choice['is_correct'])
        return 'OK'
