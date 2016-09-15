import requests
import logging

import nltk; nltk.data.path.append('nltk_data')

from .models import Word, Synonym
from . import filters as flt


logger = logging.getLogger(__name__)


def exclude_by_type(
    text, word_types=flt.TYPES,
    wordparts=flt.EXCLUDE_WORDPARTS):
    """
    exclude items by type function
    """
    if type(text) is not list:
        text = nltk.word_tokenize(text)

    text = list(set(text))
    
    for word in text:
        if len(word)>1 and word.startswith('#'):
            word = word[1:]

    text = nltk.pos_tag(text)  # tag word with a type
    cleaned_list = []
    for word, word_type in text:
        skip_word = False
        for lang in flt.AVAILABLE_LANGUAGES:
            english_word = False
            if lang.check(word):
                english_word = True
            
            if not english_word:
                skip_word = True

        if skip_word:
            continue
        
        if word_type not in word_types:
            skip_word = True
        
        if skip_word:
            continue

        for part in wordparts:
            if part in word:
                skip_word = True

        if skip_word:
            continue

        cleaned_list.append(word)
    return cleaned_list
