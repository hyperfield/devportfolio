from django.urls import path
from . import views


urlpatterns = [
    path("", views.updates_index, name="updates_index"),
    path("<int:pk>/", views.update_detail, name="update_detail"),
]
