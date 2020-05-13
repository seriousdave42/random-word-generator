from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from random_word import RandomWords

def index(request):
    return redirect('/word_generator')

def generator(request):
    r = RandomWords()
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter'] += 1
    try: 
        request.session['word'] = r.get_random_word(minLength=13, maxLength=17)
    except:
        request.session['word'] = "whoopsiedoodle"
    return render(request, "index.html")

def generate(request):
    return redirect('/word_generator')

def reset(request):
    del request.session['counter']
    return redirect('/word_generator')
