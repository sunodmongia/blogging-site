from django.urls import path
from wireium import views


urlpatterns = [
    path("", views.home, name="wireium-home"),
    path("about/", views.about, name="wireium-about"),

]
