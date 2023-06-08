from django.shortcuts import render


# Home pages menu

def home(request):
    return render(request, 'home/home.html', context={'nm':'Hello'})

def contact(request):
    return render(request, 'home/contactus.html')

def about(request):
    return render(request, 'home/aboutus.html')