from django.conf.urls import url

from . import views

app_name = 'quiz'

urlpatterns = [
    url(r'^survey/', views.survey, name='survey'),
    url(r'^listing/', views.listing, name='listing')
]