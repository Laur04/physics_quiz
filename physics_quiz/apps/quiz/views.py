from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required

from .forms import QuizForm
from .models import Profile, Option, Answer

import random
import csv

def survey(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            q1_ans, q2_ans = form.process()

            # update backend info
            for ans in q1_ans:
                for related in q1_ans:
                    opt = Option.objects.get(name=str(ans))
                    opt.increment(str(related))
                for related in q2_ans:
                    opt = Option.objects.get(name=str(ans))
                    opt.increment(str(related))
            for ans in q2_ans:
                for related in q1_ans:
                    opt = Option.objects.get(name=str(ans))
                    opt.increment(str(related))
                for related in q2_ans:
                    opt = Option.objects.get(name=str(ans))
                    opt.increment(str(related))
            
            # update for csv file
            back_dict = {'1':'Making money', '2':'Helping other people', '3': 'Having job security', '4': 'Working with people', '5': 'Having lots of family time', '6': 'Having an exciting job', '7': 'Making use of my talents/abilities', 'a': 'Medicine/Health', 'b': 'Biology', 'c': 'Chemistry', 'd': 'Physics', 'e': 'Astronomy', 'f': 'Engineering', 'g': 'English/Writing', 'h': 'Finance/Business/Consultancy', 'i': 'Administration/Management', 'j': 'Arts/Media', 'k': 'Academia/Education'}
            new_ans = Answer(ans=back_dict[str(q1_ans[0])] + ',' + back_dict[str(q1_ans[1])] + ',' + back_dict[str(q1_ans[2])] + ',' + back_dict[str(q2_ans[0])] + ',' + back_dict[str(q2_ans[1])])
            new_ans.save()
            
            # calculate results
            ans_dict = {}
            score_dict = {}
            for profile in Profile.objects.filter(Q(q2_answer=q2_ans[0]) | Q(q2_answer=q2_ans[1])):
                ans_dict.update({profile: profile.q1_convert()})
                score_dict.update({profile: 0})
            for num in q1_ans:
                for profile in ans_dict:
                    if str(num) in ans_dict[profile]:
                        score_dict[profile] += 1
            unordered_list = list()
            for profile in score_dict:
                unordered_list.append((score_dict[profile], profile))
            ordered_list = sorted(unordered_list, key=lambda score: score[0], reverse=True)
            final_ordered_list = list()
            count = 0
            for item in ordered_list:
                if count < 6:
                    final_ordered_list.append(item[1])
                    count += 1
            for n in range(0, len(q2_ans)):
                q2_ans[n] = str(q2_ans[n])
            tag_list = list()
            ans_list = list()
            ans_list.append(q1_ans[0]); ans_list.append(q1_ans[1]); ans_list.append(q1_ans[2]); ans_list.append(q2_ans[0]); ans_list.append(q2_ans[1])
            for profile in final_ordered_list:
                tag_list.append((profile, ', '.join(profile.compare_ans(ans_list))))
            
            # return
            return render(request, 'quiz/results.html', context={'profiles':tag_list})
        return render(request, 'quiz/questions.html', context={'form':form})
    else:
        form = QuizForm()
        return render(request, 'quiz/questions.html', context={'form':form})

def listing(request):
    profiles = list()
    for p in Profile.objects.all():
        profiles.append(p)
    random.shuffle(profiles)
    return render(request, 'quiz/list.html', context={'profiles':profiles})

@login_required
def statistics(request):
    user = request.user
    if user.username == "site_superuser" or user.username == "site_staff":
        opts = Option.objects.all()
        if request.method == 'POST':
            for o in opts:
                o.reset()
            answers = Answer.objects.all()
            for a in answers:
                a.delete()
            return HttpResponseRedirect(reverse('quiz:statistics'))
        else:
            # count self
            self_counts_q1 = list()
            self_counts_q2 = list()
            num = 0
            for o in opts:
                if num < 11:
                    self_counts_q1.append(o.self_count(o.name))
                else:
                    self_counts_q2.append(o.self_count(o.name))
                num += 1

            ctx = {'self_counts_q1':self_counts_q1, 'self_counts_q2':self_counts_q2}
            return render(request, 'quiz/stats.html', context=ctx)
    else:
        return HttpResponse("You are not authorized to view this page.")

@login_required
def getfile(request):
    user = request.user
    if user.username == "site_superuser" or user.username == "site_staff":
        response = HttpResponse(content_type='text/csv')  
        response['Content-Disposition'] = 'attachment; filename="answer_stats.csv"'
        writer = csv.writer(response)
        for a in Answer.objects.all():
            new_list = a.ans.split(', ')
            writer.writerow(new_list) 
        return response
    else:
        return HttpResponse("You are not authorized to view this page.")