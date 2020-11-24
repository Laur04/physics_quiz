from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'classroom'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('classroom/', views.classroom, name='classroom'),
    path('response/', views.response, name='response'),
    path('changestatus/<post>/', views.changestatus, name='changestatus'),
    path('reset/student/', views.reset_student, name='reset_student'),
    path('view/<post>/', views.view_pdf, name='view_pdf'),
]