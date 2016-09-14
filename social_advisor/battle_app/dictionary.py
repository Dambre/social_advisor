import requests

import nltk; nltk.data.path.append('nltk_data')

from .models import Word, Synonym
from . import filters as flt


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


def create_synonyms(orig_word):
    '''
    funation for creating synonyms by passing word
    '''
    try:
        headers = {
            "X-Mashape-Key": "aIder4iWr4msh5Scn073WRoddmAEp1qA0I3jsnSR8lfJwtyzpg",
            "Accept": "application/json"}

        response = requests.get("https://wordsapiv1.p.mashape.com/words/{}/synonyms".format(orig_word), headers=headers)
        if response.status_code == 200:
            json = response.json()
            synonyms = json['synonyms']
            # synonyms = nltk.word_tokenize(synonyms)
            synonyms = nltk.pos_tag(synonyms)
            word = nltk.word_tokenize(orig_word)
            word = nltk.pos_tag(word)[0]
            print(synonyms)
            good_syns = []
            for syn in synonyms:
                print(word[1], syn[1])
                if word[1] == syn[1]:
                    print('*')
                    good_syns.append(syn[0])
            word = Word.objects.get_or_create(word=orig_word)            
            for syn in good_syns[:2]:
                try:
                    new_word = Word.objects.create(word=syn.lower(), is_synonym=True)
                except Exception:
                    new_word = Word.objects.get(word=word)
                syn = Synonym.objects.create(word=new_word)
                syn.synonym_to.add(word)
            return good_syns
    except Exception as e:
        print(e)
