
from django.core.management.base import BaseCommand, CommandError

from battle_app.models import Word
from battle_app.twitter import get_word_statistics


class Command(BaseCommand):
    '''
    Class to clean data
    '''
    def handle(self, *args, **kwargs):
        return

if __name__ == '__main__':
    Command.handle()