
import requests

from django.db import transaction

from bs4 import BeautifulSoup
import nltk; nltk.data.path.append('nltk_data')

from battle_app.dictionary import exclude_by_type
from battle_app.models import Word, Synonym


URL = 'http://www.synonym.com/synonyms/{}'


def scrape(word):
    response = requests.get(URL.format(word))
    soup = BeautifulSoup(response.text, 'html.parser')
    synonyms = soup.find_all('li', class_='syn')
    synonyms = list(filter(
        lambda syn: len(syn.split()) < 2,
        [syn.a.text for syn in synonyms]))

    synonyms = nltk.pos_tag(exclude_by_type(synonyms))
    word = Word.objects.get(word=word)
    with transaction.atomic():
        for synonym, type in synonyms:
            syn, created = Word.objects.get_or_create(
                word=synonym, type=type)
            Synonym.objects.create(word=word, synonym_to=syn)        
