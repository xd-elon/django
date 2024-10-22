from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from blog import views as blog_views
from home import views as home_views


urlpatterns = [
    path('blog/', blog_views.blog),
    path('', home_views.home),
]
