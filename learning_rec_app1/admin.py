from django.contrib import admin

# Register your models here.
#Here, we are importing the topic class from the models directory
from .models import Entry, Topic
admin.site.register(Topic)
admin.site.register(Entry)