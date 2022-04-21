from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    if request.method == 'POST':
        context = {'text': 'POST METHOD!!!'}
        return render(request, 'accountapp/hello_world.html', context)
    else:
        context = {'text': 'GET METHOD!!!'}
        return render(request, 'accountapp/hello_world.html', context)