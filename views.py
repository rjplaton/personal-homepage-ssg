import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    content_html = open("content/index.html").read()
    context = {
    "content": content_html, 
    }
    return render(request, "index.html", context)

def projects(request):
    content_html = open("content/projects.html").read()
    context = {
    "content": content_html, 
    }
    return render(request, "projects.html", context)

def blog(request):
    content_html = open("content/blog.html").read()
    context = {
    "content": content_html, 
    }
    return render(request, "blog.html", context)

def contact(request):
    content_html = open("content/contact.html").read()
    context = {
    "content": content_html, 
    }
    return render(request, "contact.html", context)


def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/michaelpb/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

