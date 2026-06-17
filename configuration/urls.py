from django.urls import path
from . import views

app_name = "configuration"

urlpatterns = [
    path("", views.configMain, name="main"),
    path("unit/", views.unitConfig, name="unit"),
    path("unit/creation", views.unitCreation, name="unit_create"),
]