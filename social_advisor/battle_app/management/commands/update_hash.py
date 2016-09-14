
from django.core.management.base import BaseCommand, CommandError

from battle_app.models import Word
from battle_app.twitter import get_word_statistics


class Command(BaseCommand):
    '''
    Class to get hashtags score
    '''
    def handle(self, *args, **kwargs):
        words = Word.objects.all().order_by('updated_at')[:460]
        for word in words:
            print(word.word)
            get_word_statistics(word)
        return

if __name__ == '__main__':
    Command.handle()