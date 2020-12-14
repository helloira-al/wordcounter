from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request, 'home.html') 

def result(request):
	text = request.GET['text']

	words = text.split()

	word_dict = {}

	for word in words:
		if word in word_dict:
			word_dict[word] +=1
		else:
			word_dict[word] = 1

	return render(request, 'result.html', {'text': text, 'count': len(words)})

def about(request):
	return render(request, 'about.html')