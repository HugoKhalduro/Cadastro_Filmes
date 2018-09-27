from django.shortcuts import render

# Create your views here.
def minha_view(request) :
    return render(request, 'minha_view.html', {})