from django.urls import path
from . import views

app_name = "inventory"

urlpatterns = [
    path("", views.inventory, name="main"),
    path("create/", views.create, name="create"),
]