from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
        #return self.order_by('-id')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=255, default='')
    text = models.TextField(default='')
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user')
    c_objects = QuestionManager()
    objects = models.Manager()
 
    def get_url(self):
        return '/question/{}/'.format(self.id)

    def __unicode__(self):
        return self.title 

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()
    
    def __unicode__(self):
        return self.text
