from django.shortcuts import render, redirect, get_object_or_404
from .models import Classroom, Assignment, Quiz, Question, Choice, Submission
from .forms import ClassroomForm, AssignmentForm, QuizForm, QuestionForm, ChoiceForm, SubmissionForm

def index(request):
    return render(request, 'core/index.html')

def create_classroom(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            classroom = form.save(commit=False)
            classroom.teacher = request.user
            classroom.save()
            return redirect('home')
    else:
        form = ClassroomForm()
    return render(request, 'core/create_classroom.html', {'form': form})

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
