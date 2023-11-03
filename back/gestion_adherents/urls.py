from django.urls import path
from gestion_adherents import views

urlpatterns = [
    path("members.json", views.members),
    path("members/<int:pk>", views.member_detail),
]
