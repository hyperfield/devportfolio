from django.urls import path
from . import views


urlpatterns = [
    path("", views.whatido_index, name="whatido_index"),
]
