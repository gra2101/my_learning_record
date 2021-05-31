#This part defines the url pattern for learning record home pge

from django.conf.urls import url
from django.urls import path
from . import views
app_name='learning_rec_app1'
urlpatterns=[
    #home page
    path('',views.index,name='index'),
    #topic page
    path('topics/',views.topics, name='topics'),
    #page for a simple topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #page for adding new topic
    path('new_topic/',views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]