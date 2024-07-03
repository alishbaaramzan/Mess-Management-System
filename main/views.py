from django.shortcuts import render

# Create your views here.
def mainIndex(request):
    return render(request, 'main/index.html')