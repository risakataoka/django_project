from django.shortcuts import render


def index(request):
    return render(request, 'todo/top_page.html')


def top_page(request):
    return render(request, 'todo/top_page.html', {})
