from django.contrib import admin
from .models import Word, WordUsage, Synonym

class WordUsageAdmin(admin.ModelAdmin):
	model = WordUsage
	list_display = ('word', 'retweets', 'likes', 'timestamp')


class WordAdmin(admin.ModelAdmin):
	model = Word
	readonly_fields = ('word', 'word_type', 'updated_at', 'created_at', 'last_tweet_id')
	list_display = ('word', 'word_type')


class SynonymAdmin(admin.ModelAdmin):
	model = Synonym
	readonly_fields = ('word', 'synonym_to')

admin.site.register(Word, WordAdmin)
admin.site.register(WordUsage, WordUsageAdmin)
admin.site.register(Synonym, SynonymAdmin)
