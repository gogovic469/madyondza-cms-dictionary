from django.shortcuts import render_to_response
from django.shortcuts import render
from models import Entry

def home(request):
    heading = 'Madyondza Dictionary'
    return render_to_response('home.html', {'heading': heading})

def all_words(request):
    words = Entry.objects.order_by('word')
    return render(request, 'words.html', {'words': words})
