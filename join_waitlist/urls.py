from django.urls import path
from . import views

app_name = 'join_waitlist'
urlpatterns = [
    path('join-waitlist', views.join_waitlist, name='join_waitlist'),
]