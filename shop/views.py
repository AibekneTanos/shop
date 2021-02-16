from django.shortcuts import render

def view_dishes(request):
    return render(request, "index.html")