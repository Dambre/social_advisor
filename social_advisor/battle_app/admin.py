from django.contrib import admin
from .models import *

class WordUsageAdmin(admin.ModelAdmin):
	model = WordUsage
	list_display = ('word', 'retweets', 'likes', 'timestamp')

admin.site.register(Word)
admin.site.register(WordUsage, WordUsageAdmin)
admin.site.register(Synonym)
