from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("injection", views.injectionView, name="injection"),
    path("information", views.informationView, name="information"),
]
