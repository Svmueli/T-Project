from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('instructor_dashboard/', views.instructor_dashboard, name='instructor_dashboard'),
    path('create_classroom/', views.create_classroom, name='create_classroom'),
    path('join_classroom/', views.join_classroom, name='join_classroom'),
    path('classroom/<int:classroom_id>/', views.classroom_detail, name='classroom_detail'),
    path('create_assignment/<int:classroom_id>/', views.create_assignment, name='create_assignment'),
    path('assignment/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),
    path('submit_assignment/<int:assignment_id>/', views.submit_assignment, name='submit_assignment'),
    path('create_quiz/<int:classroom_id>/', views.create_quiz, name='create_quiz'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('create_announcement/<int:classroom_id>/', views.create_announcement, name='create_announcement'),
    path('create_comment/<int:classroom_id>/', views.create_comment, name='create_comment'),
    path('profile/', views.profile, name='profile'),
    path('inbox/', views.inbox, name='inbox'),
    path('send_message/', views.send_message, name='send_message'),
]
