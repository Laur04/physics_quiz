from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

from .forms import QuizForm
from .models import Profile, Option

import random

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

def statistics(request):
    opts = Option.objects.all()

    # count self
    self_counts_q1 = list()
    self_counts_q2 = list()
    num = 0
    for o in opts:
        if num < 7:
            self_counts_q2.append(o.self_count(o.name))
        else:
            self_counts_q1.append(o.self_count(o.name))
        num += 1

    # other stats
    q1_to_q1 = list()
    q1_to_q2 = list()
    q2_to_q1 = list()
    q2_to_q2 = list()
    for o in opts:
        if o.name in ['1', '2', '3', '4', '5', '6', '7']:
            q1_to_q1.append(o.compare_to_q1(o.name))
            q1_to_q2.append(o.compare_to_q2(o.name))
        elif o.name in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']:
            q2_to_q1.append(o.compare_to_q1(o.name))
            q2_to_q2.append(o.compare_to_q2(o.name))

    ctx = {'self_counts_q1':self_counts_q1, 'self_counts_q2':self_counts_q2, 'q1_to_q1':q1_to_q1, 'q2_to_q2':q2_to_q2, 'q2_to_q1':q2_to_q1, 'q1_to_q2':q1_to_q2}
    return render(request, 'quiz/stats.html', context=ctx)

def reset(response):
    opt = Option.objects.all()
    for o in opt:
        o.reset()
    return HttpResponseRedirect(reverse('home:index'))
