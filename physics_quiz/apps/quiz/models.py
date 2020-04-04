from django.db import models

from multiselectfield import MultiSelectField

class Profile(models.Model):

    q1_choices = ((1, 'Making money'), (2, 'Helping other people'), (3, 'Having job security'), (4, 'Working with people'), (5, 'Having lots of family time'), (6, 'Having an exciting job'), (7, 'Making use of my talents/abilities'))
    q2_choices = (('a', 'Medicine/Health'), ('b', 'Biology'), ('c', 'Chemistry'), ('d', 'Physics'), ('e', 'Astronomy'), ('f', 'Engineering'), ('g', 'English/Writing'), ('h', 'Finance/Business/Consultancy'), ('i', 'Administration/Management'), ('j', 'Arts/Media'), ('k', 'Academia/Education'))

    name = models.CharField('Name', unique=True, max_length=100)
    job = models.CharField('Job Title', max_length=100)
    description = models.CharField('Description', max_length=10000)
    link = models.CharField('Link', max_length=200)
    image = models.ImageField(upload_to='profile_photos/')
    q1_answer = MultiSelectField(choices=q1_choices)
    q2_answer = MultiSelectField(choices=q2_choices, max_choices=1)

    def __str__(self):
        return self.name

    def q1_convert(self):
        q1_dict = {'Making money': 1, 'Helping other people': 2, 'Having job security': 3, 'Working with people': 4, 'Having lots of family time': 5, 'Having an exciting job': 6, 'Making use of my talents/abilities': 7}
        num_list = list()
        for i in str(self.q1_answer).split(', '):
            num_list.append(str(q1_dict[i]))
        return num_list

    def q2_convert(self):
        q2_dict = {'Medicine/Health':'a', 'Biology':'b', 'Chemistry':'c', 'Physics':'d', 'Astronomy':'e', 'Engineering':'f', 'English/Writing':'g', 'Finance/Business/Consultancy':'h', 'Administration/Management':'i', 'Arts/Media':'j', 'Academia/Education':'k'}
        num_list = list()
        for i in str(self.q2_answer).split(', '):
            num_list.append(q2_dict[i])
        return num_list

    def compare_ans(self, me_ans):
        q1 = self.q1_convert()
        q2 = self.q2_convert()
        common = list()
        for num in q1:
            if str(num) in me_ans:
                common.append(num)
        for num in q2:
            if num in me_ans:
                common.append(num)
        back_dict = {'1':'Making money', '2':'Helping other people', '3': 'Having job security', '4': 'Working with people', '5': 'Having lots of family time', '6': 'Having an exciting job', '7': 'Making use of my talents/abilities', 'a': 'Medicine/Health', 'b': 'Biology', 'c': 'Chemistry', 'd': 'Physics', 'e': 'Astronomy', 'f': 'Engineering', 'g': 'English/Writing', 'h': 'Finance/Business/Consultancy', 'i': 'Administration/Management', 'j': 'Arts/Media', 'k': 'Academia/Education'}
        common_word = list()
        for num in common:
            common_word.append(back_dict[num])
        return common_word
