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

class Option(models.Model):
    answers = (('a', 'Medicine/Health'), ('b', 'Biology'), ('c', 'Chemistry'), ('d', 'Physics'), ('e', 'Astronomy'), ('f', 'Engineering'), ('g', 'English/Writing'), ('h', 'Finance/Business/Consultancy'), ('i', 'Administration/Management'), ('j', 'Arts/Media'), ('k', 'Academia/Education'), ('1', 'Making money'), ('2', 'Helping other people'), ('3', 'Having job security'), ('4', 'Working with people'), ('5', 'Having lots of family time'), ('6', 'Having an exciting job'), ('7', 'Making use of my talents/abilities'))

    name = models.CharField('Name', unique=True, max_length=1, primary_key=True, choices=answers)
    o_1 = models.IntegerField('Frequency O1', default=0)
    o_2 = models.IntegerField('Frequency O2', default=0)
    o_3 = models.IntegerField('Frequency O3', default=0)
    o_4 = models.IntegerField('Frequency O4', default=0)
    o_5 = models.IntegerField('Frequency O5', default=0)
    o_6 = models.IntegerField('Frequency O6', default=0)
    o_7 = models.IntegerField('Frequency O7', default=0)
    o_a = models.IntegerField('Frequency Oa', default=0)
    o_b = models.IntegerField('Frequency Ob', default=0)
    o_c = models.IntegerField('Frequency Oc', default=0)
    o_d = models.IntegerField('Frequency Od', default=0)
    o_e = models.IntegerField('Frequency Oe', default=0)
    o_f = models.IntegerField('Frequency Of', default=0)
    o_g = models.IntegerField('Frequency Og', default=0)
    o_h = models.IntegerField('Frequency Oh', default=0)
    o_i = models.IntegerField('Frequency Oi', default=0)
    o_j = models.IntegerField('Frequency Oj', default=0)
    o_k = models.IntegerField('Frequency Ok', default=0)

    def increment(self, ans):
        if ans == '1':
            self.o_1 = self.o_1 + 1
        elif ans == '2':
            self.o_2 = self.o_2 + 1
        elif ans == '3':
            self.o_3 = self.o_3 + 1
        elif ans == '4':
            self.o_4 = self.o_4 + 1
        elif ans == '5':
            self.o_5 = self.o_5 + 1
        elif ans == '6':
            self.o_6 = self.o_6 + 1
        elif ans == '7':
            self.o_7 = self.o_7 + 1
        elif ans == 'a':
            self.o_a = self.o_a + 1
        elif ans == 'b':
            self.o_b = self.o_b + 1
        elif ans == 'c':
            self.o_c = self.o_c + 1
        elif ans == 'd':
            self.o_d = self.o_d + 1
        elif ans == 'e':
            self.o_e = self.o_e + 1
        elif ans == 'f':
            self.o_f = self.o_f + 1
        elif ans == 'g':
            self.o_g = self.o_g + 1
        elif ans == 'h':
            self.o_h = self.o_h + 1
        elif ans == 'i':
            self.o_i = self.o_i + 1
        elif ans == 'j':
            self.o_j = self.o_j + 1
        elif ans == 'k':
            self.o_k = self.o_k + 1
        self.save()
    
    def reset(self):
        self.o_1 = 0
        self.o_2 = 0
        self.o_3 = 0
        self.o_4 = 0
        self.o_5 = 0
        self.o_6 = 0
        self.o_7 = 0
        self.o_a = 0
        self.o_b = 0
        self.o_c = 0
        self.o_d = 0
        self.o_e = 0
        self.o_f = 0
        self.o_g = 0
        self.o_h = 0
        self.o_i = 0
        self.o_j = 0
        self.o_k = 0
        self.save()
    
    def self_count(self, who):
        answers = {'a':('Medicine/Health', self.o_a), 'b':('Biology', self.o_b), 'c':('Chemistry', self.o_c), 'd':('Physics', self.o_d), 'e':('Astronomy', self.o_e), 'f':('Engineering', self.o_f), 'g':('English/Writing', self.o_g), 'h':('Finance/Business/Consultancy', self.o_h), 'i':('Administration/Management', self.o_i), 'j':('Arts/Media', self.o_j), 'k':('Academia/Education', self.o_k), '1':('Making money', self.o_1), '2':('Helping other people', self.o_2), '3':('Having job security', self.o_3), '4':('Working with people', self.o_4), '5':('Having lots of family time', self.o_5), '6':('Having an exciting job', self.o_6), '7': ('Making use of my talents/abilities', self.o_7)}
        return answers[who]

    def compare_to_q1(self, who):
        who = str(who)
        ans = list()
        answers_alt = {'a':('Medicine/Health', self.o_a), 'b':('Biology', self.o_b), 'c':('Chemistry', self.o_c), 'd':('Physics', self.o_d), 'e':('Astronomy', self.o_e), 'f':('Engineering', self.o_f), 'g':('English/Writing', self.o_g), 'h':('Finance/Business/Consultancy', self.o_h), 'i':('Administration/Management', self.o_i), 'j':('Arts/Media', self.o_j), 'k':('Academia/Education', self.o_k)}
        answers = {'1':('Making money', self.o_1), '2':('Helping other people', self.o_2), '3':('Having job security', self.o_3), '4':('Working with people', self.o_4), '5':('Having lots of family time', self.o_5), '6':('Having an exciting job', self.o_6), '7': ('Making use of my talents/abilities', self.o_7)}
        for a in answers:
            if a != who and answers[a][1] != 0:
                ans.append(answers[a])
        if ans:
            sorted_ans = sorted(ans, key=lambda ans: ans[1], reverse=True)
        else:
            sorted_ans = list()
        if who in ['1', '2', '3', '4', '5', '6', '7']:
            return (answers[who][0], sorted_ans)
        else:
            return (answers_alt[who][0], sorted_ans)

    def compare_to_q2(self, who):
        who = str(who)
        answers_alt = {'1':('Making money', self.o_1), '2':('Helping other people', self.o_2), '3':('Having job security', self.o_3), '4':('Working with people', self.o_4), '5':('Having lots of family time', self.o_5), '6':('Having an exciting job', self.o_6), '7': ('Making use of my talents/abilities', self.o_7)}
        answers = {'a':('Medicine/Health', self.o_a), 'b':('Biology', self.o_b), 'c':('Chemistry', self.o_c), 'd':('Physics', self.o_d), 'e':('Astronomy', self.o_e), 'f':('Engineering', self.o_f), 'g':('English/Writing', self.o_g), 'h':('Finance/Business/Consultancy', self.o_h), 'i':('Administration/Management', self.o_i), 'j':('Arts/Media', self.o_j), 'k':('Academia/Education', self.o_k)}
        ans = list()
        for a in answers:
            if a != who and answers[a][1] != 0:
                ans.append(answers[a])
        if ans:
            sorted_ans = sorted(ans, key=lambda ans: ans[1], reverse=True)
        else:
            sorted_ans = list()
        if who in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']:
            return (answers[who][0], sorted_ans)
        else:
            return (answers_alt[who][0], sorted_ans)

    def __str__(self):
        return str(self.name)
