from django.db import models
from django.contrib.auth.models import User

class Classes(models.Model):
    name = models.CharField('Class Name', unique=True, max_length=30)
    teacher = models.OneToOneField(User, related_name='class_teacher', on_delete=models.CASCADE)
    student = models.OneToOneField(User, related_name='class_student', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
class Post(models.Model):
    post_id = models.CharField(max_length=40)
    name = models.CharField(max_length=80)
    position = models.CharField(max_length=80)
    company = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    school = models.CharField(max_length=80)
    degree = models.CharField(max_length=80)
    experience = models.CharField(max_length=400)
    education = models.CharField(max_length=400)
    skills = models.CharField(max_length=400)
    endorsements = models.CharField(max_length=400)
    hidden = models.BooleanField(default=True)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer

    def changeStatus(self):
        if self.hidden == True:
            self.hidden = False
        else:
            self.hidden = True
        self.save()