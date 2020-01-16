from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]
