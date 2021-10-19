from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    #date_posted = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     #return (self.title+" by "+self.author)
    #     return self.title