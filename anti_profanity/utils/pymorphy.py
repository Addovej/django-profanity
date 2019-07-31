import re

from django.apps import apps
import pymorphy2

from anti_profanity.models import Profanity

__all__ = ['PymorphyProc']

word_pattern = r'[А-яA-z0-9\-]+'


class PymorphyProc(object):
    morph = pymorphy2.MorphAnalyzer()

    @staticmethod
    def detect(text):
        return [w for w in PymorphyProc._gen(text)] if text else []

    @staticmethod
    def replace(text, repl='[censored]'):
        for word in PymorphyProc._gen(text):
            text = text.replace(word, repl)
        return text

    @staticmethod
    def wrap(text, wrap=('<span style="color:red;">', '</span>',)):
        words = {}
        for word in PymorphyProc._gen(text):
            words[word] = f'{wrap[0]}{word}{wrap[1]}'
        for word, wrapped in words.items():
            text = text.replace(word, wrapped)
        return text

    @staticmethod
    def _gen(text):
        words = PymorphyProc.get_words()
        for word in re.findall(word_pattern, text):
            if len(word) < 3:
                continue
            normal_word = PymorphyProc.morph.parse(word.lower())[0].normal_form
            if normal_word in words:
                yield word

    @staticmethod
    def get_words():
        return Profanity.objects.values_list('word', flat=True)
