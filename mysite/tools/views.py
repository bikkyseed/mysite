from django.shortcuts import render

# Create your views here.

def tools(request):
    return render(request, 'tools/tools.html')

def title_generator(request):
    return render(request, 'tools/title-generator.html')
