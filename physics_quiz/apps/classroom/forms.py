from django import forms

class CreateForm(forms.Form):
    class_name = forms.CharField(max_length=30, required=True)
    teacher_username = forms.CharField(max_length=30, required=True)
    teacher_password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput)
    teacher_email = forms.EmailField(required=True)
    student_username = forms.CharField(max_length=30, required=True)
    student_password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput)

class SurveyForm(forms.Form):
    COLOR_CHOICES = ((1, 'red'), (2, 'blue'), (3, 'purple'), (4, 'yellow'), (5, 'green'))

    name = forms.CharField(max_length=80, required=True)
    position = forms.CharField(max_length=80, required=True)
    company = forms.CharField(max_length=80, required=True)
    location = forms.CharField(max_length=80, required=True)
    school = forms.CharField(max_length=80, required=True)
    degree = forms.CharField(max_length=80, required=True)
    experience = forms.CharField(max_length=400, required=True, widget=forms.Textarea)
    skills = forms.CharField(max_length=400, required=True, widget=forms.Textarea)
    endorsements = forms.CharField(max_length=400, required=True, widget=forms.Textarea)
    profile_pic = forms.ImageField(required=True)
    background_color = forms.ChoiceField(choices=COLOR_CHOICES, required=True)

class StudentResetForm(forms.Form):
    new_password1 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput)
    new_password2 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput)

    def is_valid(self):
        valid = super(StudentResetForm, self).is_valid()
        return self.cleaned_data["new_password1"] == self.cleaned_data["new_password2"]
