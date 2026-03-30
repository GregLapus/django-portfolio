from django.shortcuts import render


def index(request):
    """Render the index/home page"""
    return render(request, 'portfolio/index.html')


def about(request):
    """Render the about page"""
    return render(request, 'portfolio/about.html')


def projects(request):
    """Render the projects page"""
    return render(request, 'portfolio/projects.html')


def other_skills(request):
    """Render the other skills page"""
    return render(request, 'portfolio/other_skills.html')
