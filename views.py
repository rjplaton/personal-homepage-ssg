import requests
from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
import os

mailgun_api_key = os.environ["MAILGUN_API_KEY"]

def index(request):
    context = {
    }
    return render(request, "index.html", context)

def projects(request):
    context = {
    }
    return render(request, "projects.html", context)
    
def repos(request):
    response = requests.get('https://api.github.com/users/rjplaton/repos')
    repos = response.json()
    context = {
    "github_repos": repos,
    }
    return render(request, "repos.html", context)

def blog(request):
    context = {
    }
    return render(request, "blog.html", context)

def contact(request):
    context = { 
    }
    return render(request, "contact.html", context)

def blog_post(request):
    context = {
    }
    return render(request, "blog_base.html", context)

def send_email(request):
    name = request.POST["name"]
    email = request.POST["email"]
    subject = "Hello from", name, " - Contact Form Submission"
    message = '''
    Name:''', name, """
    Message:""", request.POST["message"]
    requests.post(
        "https://api.mailgun.net/v3/rjplaton.com/messages",
        auth=(
            "api", mailgun_api_key
            ),
        data={
            "from": "contact@rjplaton.com",
            "to": "rjplaton@gmail.com",
            "subject": subject,
            "text": message, 
            }
        )
    return redirect("contact.html") # Return a redirect!

