from django.urls import path
from . import views

urlpatterns = [
    path("add-learning/", views.add_learning, name="add_learning"),
]