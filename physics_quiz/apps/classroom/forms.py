from django import forms

class CreateForm(forms.Form):
    class_name = forms.CharField(max_length=30, required=True)
    teacher_username = forms.CharField(max_length=30, required=True)
    teacher_password = forms.CharField(max_length=30, required=True)
    teacher_email = forms.EmailField(required=True)
    student_username = forms.CharField(max_length=30, required=True)
    student_password = forms.CharField(max_length=30, required=True)

class SurveyForm(forms.Form):
    ans = forms.CharField(widget=forms.Textarea, max_length=10000)
