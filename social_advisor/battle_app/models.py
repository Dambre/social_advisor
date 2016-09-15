import uuid
import pytz

from django.utils import timezone
from datetime import datetime
from django.db import models



NN = 'NN'
ADJ = 'ADJ'
ADV = 'ADV'
V = 'V'

WORD_TYPES = (
    (NN, 'Noun'),
    (ADJ, 'Adjective'),
    (ADV, 'Adverb'),
    (V, 'Verb')
)


class Word(models.Model):
    id = models.UUIDField(primary_key=True, 
        default=uuid.uuid4, editable=False)
    word = models.CharField(max_length=140, unique=True, editable=False)
    type = models.CharField(choices=WORD_TYPES, max_length=5, null=True)
    last_tweet_id = models.CharField(max_length=50, default='0', editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ('-updated_at',)

    def __str__(self):
        return self.word

    def save(self, *args, **kwargs):
        self.word = self.word.lower()
        super(Word, self).save(*args, **kwargs)
    
    def update_latest_id(self, tweet_id):
        if int(self.last_tweet_id) < tweet_id:
            self.last_tweet_id = str(tweet_id)
        self.save()


class Synonym(models.Model):
    synonym_to = models.ForeignKey(Word, related_name='synonym_to_word', null=True)
    word = models.ForeignKey(Word)

    class Meta:
        unique_together = (('synonym_to', 'word'),)


class WordUsage(models.Model):
    word = models.ForeignKey(Word)
    retweets = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.word.word


class Setting(models.Model):
    key = models.CharField(max_length=200, unique=True)
    value = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.key

    def activate(self):
        self.active = True
        self.save()
        return 'Setting activated.'

    def deactivate(self):
        self.active = False
        self.save()
        return 'Setting deactivated.'
