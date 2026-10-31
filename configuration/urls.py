from django.urls import path
from . import views

app_name = "configuration"

urlpatterns = [
    path("", views.configMain, name="main"),
    
    path("unit/", views.unitMain, name="unit"),
    path("unit/creation", views.unitCreation, name="unit_create"),
    path("unit/modify/<int:unit_id>/", views.unitModify, name="unit_modify"),
    path("unit/delete/<int:unit_id>/", views.unit_delete, name="unit_delete"),

    path("category/", views.categoryMain, name="category"),
    path("category/creation", views.categoryCreation, name="category_create"),
]