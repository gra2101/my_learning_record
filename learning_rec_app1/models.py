from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    #for the topic the user has learnt
    text=models.CharField(max_length=50)
    date_added=models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        #this should retuen a string representation of the model
        return self.text

class Entry(models.Model):
    #to allow user enter what he has learnt about a topic
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    text=models.TextField()
    date_added= models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural='Entries'
    def __str__(self):
        #returns a string representation of the model
        if len(self.text) < 50:
            return self.text
        else:
            return f"{self.text[:50]}...."
