import datetime

from django.db import models
from django.utils import timezone

"""
A model contains the essential fields & behaviors of the stored data; they are how we define the data.
Three stsp for editing a model:
---change model in models.py
---Run 'python manage.py makemigrations' to create migrations for changes
---Run 'python manage.py migrate' to apply changes to database
"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now()
datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
