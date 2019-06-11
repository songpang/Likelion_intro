from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'home.html')
  ### render는 3가지 인자까지 받을 수 있음
  ### 1번째는 request, 2번째는 템플릿, 3번쨰는 딕셔너리 형 인자 받을 수 있음.

def about(request):
  return render(request, 'about.html')

def result(request):
  text = request.GET['fulltext']
  words = text.split()
  word_dictionary = {}

  for word in words:
    if word in word_dictionary:
      word_dictionary[word] += 1
    else:
      word_dictionary[word] = 1

  return render(request, 'result.html',\
     {'full': text, \
      'total' : len(words), \
      'dictionary': word_dictionary.items()})
