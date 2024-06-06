from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import (
    UserRegisterForm, ProfileForm, ClassroomForm, AssignmentForm, QuizForm, 
    AnnouncementForm, CommentForm, UserProfileForm, MessageForm, AssignmentSubmissionForm
)
from .models import Classroom, Assignment, Quiz, Announcement, Comment, UserProfile, Message, AssignmentSubmission, Profile

def home(request):
    return render(request, 'core/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_dashboard' if user.profile.role == 'student' else 'instructor_dashboard')
    return render(request, 'core/login.html')

@login_required
def student_dashboard(request):
    return render(request, 'core/student_dashboard.html')

@login_required
def instructor_dashboard(request):
    return render(request, 'core/instructor_dashboard.html')

@login_required
def create_classroom(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            classroom = form.save(commit=False)
            classroom.instructor = request.user
            classroom.save()
            return redirect('instructor_dashboard')
    else:
        form = ClassroomForm()
    return render(request, 'core/create_classroom.html', {'form': form})

@login_required
def join_classroom(request):
    if request.method == 'POST':
        code = request.POST['code']
        try:
            classroom = Classroom.objects.get(code=code)
            classroom.students.add(request.user)
            return redirect('student_dashboard')
        except Classroom.DoesNotExist:
            return redirect('join_classroom')
    return render(request, 'core/join_classroom.html')

@login_required
def classroom_detail(request, classroom_id):
    classroom = get_object_or_404(Classroom, id=classroom_id)
    assignments = classroom.assignment_set.all()
    quizzes = classroom.quiz_set.all()
    announcements = classroom.announcement_set.all()
    comments = classroom.comment_set.all()
    return render(request, 'core/classroom_detail.html', {
        'classroom': classroom,
        'assignments': assignments,
        'quizzes': quizzes,
        'announcements': announcements,
        'comments': comments,
    })

@login_required
def create_assignment(request, classroom_id):
    classroom = get_object_or_404(Classroom, id=classroom_id)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.classroom = classroom
            assignment.save()
            return redirect('classroom_detail', classroom_id=classroom.id)
    else:
        form = AssignmentForm()
    return render(request, 'core/create_assignment.html', {'form': form, 'classroom': classroom})

@login_required
def assignment_detail(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    return render(request, 'core/assignment_detail.html', {'assignment': assignment})

@login_required
def submit_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == 'POST':
        form = AssignmentSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.assignment = assignment
            submission.student = request.user
            submission.save()
            return redirect('assignment_detail', assignment_id=assignment.id)
    else:
        form = AssignmentSubmissionForm()
    return render(request, 'core/submit_assignment.html', {'form': form, 'assignment': assignment})

@login_required
def create_quiz(request, classroom_id):
    classroom = get_object_or_404(Classroom, id=classroom_id)
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.classroom = classroom
            quiz.save()
            return redirect('classroom_detail', classroom_id=classroom.id)
    else:
        form = QuizForm()
    return render(request, 'core/create_quiz.html', {'form': form, 'classroom': classroom})

@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'core/quiz_detail.html', {'quiz': quiz})

@login_required
def create_announcement(request, classroom_id):
    classroom = get_object_or_404(Classroom, id=classroom_id)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.classroom = classroom
            announcement.save()
            return redirect('classroom_detail', classroom_id=classroom.id)
    else:
        form = AnnouncementForm()
    return render(request, 'core/create_announcement.html', {'form': form, 'classroom': classroom})

@login_required
def create_comment(request, classroom_id):
    classroom = get_object_or_404(Classroom, id=classroom_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.classroom = classroom
            comment.user = request.user
            comment.save()
            return redirect('classroom_detail', classroom_id=classroom.id)
    return render(request, 'core/classroom_detail.html', {'form': form, 'classroom': classroom})

@login_required
def profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'core/profile.html', {'form': form})

@login_required
def inbox(request):
    received_messages = request.user.received_messages.all()
    return render(request, 'core/inbox.html', {'messages': received_messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'core/send_message.html', {'form': form})
