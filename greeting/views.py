from django.shortcuts import render

def greeting_view(request):
    return render(request, 'greetings/greetings.html')

# Create your views here.
