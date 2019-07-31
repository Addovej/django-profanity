from django.apps import apps
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load a profanity words from txt.'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        path = options['path']

