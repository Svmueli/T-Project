from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(default="Default description")

    def __str__(self):
        return self.name

class Assignment(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(default="Default description")
    due_date = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to='assignments/', default='assignments/default_file.txt')

    def __str__(self):
        return self.title

class Quiz(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(default="Default description")
    due_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Announcement(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(default="Default content")

    def __str__(self):
        return self.title

class Comment(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    content = models.TextField(default="Default comment")

    def __str__(self):
        return self.content

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="Default bio")
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField(default="Default message")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender} to {this.recipient}"

class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/')

    def __str__(self):
        return f"Submission for {self.assignment.title}"

class Profile(models.Model):
    USER_ROLES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='student')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"
