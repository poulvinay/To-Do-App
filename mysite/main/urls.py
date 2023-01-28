from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="index"),
    path("create", views.create, name="create"),
    path("<int:id>", views.point, name="pointer"),
    path("v1/", views.v1, name="view 1"),
    path("view/", views.view, name="view"),
]