from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    lineremove = request.POST.get('lineremove', 'off')
    extraspace = request.POST.get('extraspace', 'off')
    wordcount = request.POST.get('wordcount', 'off')
    analyzed_text = ''
    words = ''
    if removepunc == 'on':
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in text:
            if char not in punc:
                analyzed_text += char

    text = analyzed_text

    if lineremove == 'on':
        analyzed_text = ''
        for char in text:
            if char != '\n' and char != '\r':
                analyzed_text += char
    text = analyzed_text

    if extraspace == 'on':
        analyzed_text = ''
        for ind, char in enumerate(text):
            if not(text[ind] == ' ' and text[ind + 1] == ' '):
                analyzed_text += char
    text = analyzed_text

    if wordcount == 'on':
        count = 0
        analyzed_text = text
        text = text.strip()
        for char in text:
            if char == ' ':
                count += 1
        count += 1
        count = str(count)
        words = "Number of Words is: " + count

    params = {'analyzed_text':analyzed_text, 'words':words }
    return render(request, "analyze.html", params)