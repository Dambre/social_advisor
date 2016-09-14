
import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_POST

from .analyzer import TextAnalysis


def index(request):
	return render(request, 'battle_app/index.html')


@require_POST
@csrf_exempt
def get_user_input(request):
    user_input = request.POST.get("user_input", "")
    analysis = TextAnalysis(user_input)
    analysis.run()
    stats = {
    	'original_text': user_input,
    	'analyzed_text': analysis.improved_text,
    	'is_changed': True if user_input != analysis.improved_text else False,
    	'statistics': analysis.statistics
    }
    return JsonResponse(stats)

def get_word_statistics(request, word):
	analysis = TextAnalysis(word)
	analysis.run()
	return JsonResponse(analysis.statistics)
