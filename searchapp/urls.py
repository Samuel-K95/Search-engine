from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="homepage"),
    path('upload/', views.upload_file, name="upload"),
    path('search/', views.view_documents, name="search"),
]