from django.urls import path

from . import views


urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("projects/<str:slug>/", views.project_detail, name="project_detail"),
    path("<str:category>/", views.project_index, name="project_category"),
    path("tech/<str:technology>/", views.project_index,
         name="project_technology"),
]
