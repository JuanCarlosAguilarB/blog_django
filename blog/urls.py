from django.contrib import admin
from django.urls import path, include

from .views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="Home"),
    path("blog/", include('blog_app.urls',namespace='blog')),
]
