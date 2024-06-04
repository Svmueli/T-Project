from django import forms
from .models import Classroom, Assignment, Quiz, Question, Choice, Submission

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'file', 'due_date']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', 'is_correct']

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['file']
