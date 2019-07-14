from django.urls import path

import views

# In this example, we've separated out the views.py into a new file
urlpatterns = [
    path('', views.index),
    path('index.html', views.index),
    path('projects.html', views.projects),
    path('blog.html', views.blog),
    path('contact.html', views.contact),
    path('blog/1.html', views.blog_post),
    path('blog/2.html', views.blog_post),
    path('blog/3.html', views.blog_post),
    path('repos.html', views.repos),
    path('send-email', views.send_email),
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

