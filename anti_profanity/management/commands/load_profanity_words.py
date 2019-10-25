from django.core.management.base import BaseCommand
from tqdm import tqdm

from anti_profanity.models import Profanity


class Command(BaseCommand):
    help = 'Load a profanity words from txt.'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)
        parser.add_argument('lang', nargs='+', type=str)

    def handle(self, *args, **options):
        path = options['path'][0]
        lang = options['lang'][0]

        # Maybe need make another data files types support (csv, json etc.)
        try:
            self.stdout.write(self.style.NOTICE('Opening file...'))
            with open(path, 'r') as file:
                words = file.readlines()
        except Exception as e:
            self.stdout.write(self.style.ERROR(str(e)))
        else:
            self.stdout.write(self.style.NOTICE('Collecting...'))
            for word in tqdm(list(map(lambda x: x.strip('\n'), words)), total=len(words)):
                try:
                    Profanity.objects.create(lang=lang, word=word)
                except Exception as e:
                    self.stdout.write(self.style.ERROR(str(e)))
            self.stdout.write(self.style.SUCCESS('Import success.'))
            file.close()
