from django import forms

class QuizForm(forms.Form):

    q1_choices = ((1, 'Making money'), (2, 'Helping other people'), (3, 'Having job security'), (4, 'Working with people'), (5, 'Having lots of family time'), (6, 'Having an exciting job'), (7, 'Making use of my talents/abilities'))
    q2_choices = (('a', 'Medicine/Health'), ('b', 'Biology'), ('c', 'Chemistry'), ('d', 'Physics'), ('e', 'Astronomy'), ('f', 'Engineering'), ('g', 'English/Writing'), ('h', 'Finance/Business/Consultancy'), ('i', 'Administration/Management'), ('j', 'Arts/Media'), ('k', 'Academia/Education'))
    type_choices = (('', '----'), (0, 'Student'), (1, 'Workshop Attendee'))

    question_1 = forms.MultipleChoiceField(error_messages={'required': 'You must select exactly three items for Question 1.'}, widget = forms.CheckboxSelectMultiple, choices=q1_choices)
    question_2 = forms.MultipleChoiceField(error_messages={'required': 'You must select exactly two items for Question 2.'}, widget = forms.CheckboxSelectMultiple, choices=q2_choices)
    question_type = forms.ChoiceField(choices=type_choices, required=True)

    def is_valid(self):
        valid = super(QuizForm, self).is_valid()
        if not valid:
            return valid
        q1_ans = self.cleaned_data['question_1']
        if len(q1_ans) != 3:
            self._errors = "You must select exactly three items for Question 1."
            return False
        for n in range(0, len(q1_ans)):
            q1_ans[n] = str(q1_ans[n])
        q2_ans = self.cleaned_data['question_2']
        if len(q2_ans) != 2:
            self._errors = "You must select exactly two items for Question 2."
            return False
        return True
    
    def process(self):
        q1_ans = self.cleaned_data['question_1']
        q2_ans = self.cleaned_data['question_2']
        return (q1_ans, q2_ans)