from django.urls import path
from members import views

urlpatterns = [
    path("members/", views.members),
    path("members/<int:pk>", views.member_detail),
]
