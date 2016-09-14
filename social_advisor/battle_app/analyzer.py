from django.db.models import Sum

import nltk; nltk.data.path.append('nltk_data')

from .models import Word, WordUsage, Synonym


class TextAnalysis(object):
    """Text analysis class"""
    def __init__(self, text, max_length=140):
        super(TextAnalysis, self).__init__()
        self._text = text
        self._text_tokenized = nltk.word_tokenize(self.text)

        self._max_length = max_length
        self._analized_text = None
        self._statistics = {}
        self._words = []
        self._improved_text = ''

    @property
    def text(self):
        return self._text

    @property
    def words(self):
        return list(set(nltk.word_tokenize(self.text)))

    @property
    def text_tokenized(self):
        return self._text_tokenized
    
    @property
    def max_length(self):
        return self._max_length
    
    @property
    def analyzed_text(self):
        return self._analized_text
    
    @property
    def statistics(self):
        return self._statistics    

    @property
    def improved_text(self):
        return self._improved_text
    
    def get_synonyms(self, word_obj):
        return Synonym.objects.filter(synonym_to=word_obj)
            
    def get_words_synonyms_and_stats(self):
        all_words_with_stats = {}
        for word in self.words:
            word, created = Word.objects.get_or_create(word=word.lower())
            synonyms = []
            for syn in self.get_synonyms(word):
                synonyms.append({'word': syn.word.word, 'statistics': self.get_stats(syn.word)})
            
            all_words_with_stats.update(
                {word.word: {'statistics': self.get_stats(word), 'synonyms': synonyms}})
        
        return all_words_with_stats

    def __get_stats_dict(
        self, count=0, retweets_rate=0, likes_rate=0,
        likes=0, retweets=0, rate=0):
        return {
            'retweets_rate': retweets_rate,
            'likes_rate': likes_rate,
            'usage_count': count,
            'likes_count': likes,
            'retweets_count': retweets,
            'rate': rate,
            }

    def get_stats(self, word):
        stats = {}
        usage = WordUsage.objects.filter(word=word)
        if usage.exists():
            count = usage.count()
            retweets = 0
            likes = 0
            retweets = usage.aggregate(retweets=Sum('retweets')).get('retweets', 0)
            likes = usage.aggregate(likes=Sum('likes')).get('likes', 0)
            likes_rate = likes/count
            retweets_rate = retweets/count
            rate = (likes_rate + retweets_rate)/2
            return self.__get_stats_dict(
                count, retweets_rate, likes_rate,
                likes, retweets, rate
                )
        else:
            return self.__get_stats_dict()

    def get_better_word(self, word):
        word_rate = self.statistics[word.lower()]['statistics']['rate']
        better_word = ''
        for syn in self.statistics[word.lower()]['synonyms']:
            if word_rate < syn['statistics']['rate']:
                better_word = syn['word']
        return better_word
    
    def analyze_text(self):
        self._statistics = self.get_words_synonyms_and_stats()

    def improve_text(self):
        improved_text = self.text
        for word in self.text_tokenized:
            better_word = self.get_better_word(word)
            if better_word:
                if word.word[0].isupper():
                    better_word = better_word.capitalize()

                text.replace(word, better_word)
            self._improved_text = improved_text

    def run(self):
        self.analyze_text()
        self.improve_text()
