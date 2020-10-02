from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # default = timezone.now lets you update the date
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if user deleted then post gets deleted as well

    def __str__(self):
        return self.title