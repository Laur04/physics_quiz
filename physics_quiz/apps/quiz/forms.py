from django import forms

class QuizForm(forms.Form):

    q1_choices = ((1, 'Making money'), (2, 'Helping other people'), (3, 'Having job security'), (4, 'Working with people'), (5, 'Having lots of family time'), (6, 'Having an exciting job'), (7, 'Making use of my talents/abilities'))
    q2_choices = ((1, 'Medicine/Health'), (2, 'Biology'), (3, 'Chemistry'), (4, 'Physics'), (5, 'Astronomy'), (6, 'Engineering'), (7, 'English/Writing'), (8, 'Finance/Business/Consultancy'), (9, 'Administration/Management'), (10, 'Arts/Media'), (11, 'Academia/Education'))

    question_1 = forms.MultipleChoiceField(error_messages={'required': 'You must select exactly three items for Question 1.'}, widget = forms.CheckboxSelectMultiple, choices=q1_choices)
    question_2 = forms.MultipleChoiceField(error_messages={'required': 'You must select exactly two items for Question 2.'}, widget = forms.CheckboxSelectMultiple, choices=q2_choices)

    def is_valid(self):
        valid = super(QuizForm, self).is_valid()
        if not valid:
            return valid
        q1_ans = self.cleaned_data['question_1']
        if len(q1_ans) != 3:
            self._errors = "You must select exactly three items for Question 1."
            return False
        for n in range(0, len(q1_ans)):
            q1_ans[n] = int(q1_ans[n])
        q2_ans = self.cleaned_data['question_2']
        if len(q2_ans) != 2:
            self._errors = "You must select exactly two items for Question 2."
            return False
        return True
    
    def process(self):
        q1_ans = self.cleaned_data['question_1']
        q2_ans = self.cleaned_data['question_2']
        return (q1_ans, q2_ans)