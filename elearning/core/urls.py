from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Add this line
    path('create_classroom/', views.create_classroom, name='create_classroom'),
    path('classroom/<int:classroom_id>/create_assignment/', views.create_assignment, name='create_assignment'),
    path('classroom/<int:classroom_id>/create_quiz/', views.create_quiz, name='create_quiz'),
    # Add other URL patterns as needed
]
