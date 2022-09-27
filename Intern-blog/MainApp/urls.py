from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import blogs

app_name = "Internship"
urlpatterns = [
     path("", blogs.index, name = "Index"),
     path("blogs/<str:blog_key>/", blogs.list, name = "ViewBlog"),
     path("about/", blogs.about, name = "About"),
]