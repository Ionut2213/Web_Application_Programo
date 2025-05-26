from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Tag(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    


class NoteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_archived = False)
    


class Note(models.Model):
    IMPORTANCE_CHOICE = [
        ('low' , 'Low'),
        ('medium' , 'Medium'),
        ('high' , 'High'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    importance = models.CharField(max_length=10, choices=IMPORTANCE_CHOICE, default='low')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    attachments = models.FileField(upload_to='attachments/', null=True, blank=True)

    is_archived = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    objects = NoteManager()
    all_objects = models.Manager()

    def archive(self):
        self.is_archived = False
        self.save()

    def unarchive(self):
        self.is_archived = False
        self.save()

    def __str__(self):
        return self.title
