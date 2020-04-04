from django.conf.urls import url

from . import views

app_name = 'quiz'

urlpatterns = [
    url(r'^quiz/', views.quiz, name='quiz'),
    url(r'^listing/', views.listing, name='listing')
]