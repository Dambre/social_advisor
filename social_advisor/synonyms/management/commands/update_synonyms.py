
from django.core.management.base import BaseCommand, CommandError

from battle_app.models import Word
from synonyms.scraper import scrape


class Command(BaseCommand):
    '''
    Class to get hashtags score
    '''
    def handle(self, *args, **kwargs):
        words = Word.objects.all().order_by('-updated_at')
        for word in words:
            scrape(word.word)
        return

if __name__ == '__main__':
    Command.handle()