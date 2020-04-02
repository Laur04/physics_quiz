from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

from .forms import QuizForm
from .models import Profile

def quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            q1_ans, q2_ans = form.process()
            ans_dict = {}
            score_dict = {}
            for profile in Profile.objects.filter(Q(q2_answer=q2_ans[0]) | Q(q2_answer=q2_ans[1])):
                ans_dict.update({profile: profile.q1_convert()})
                score_dict.update({profile: 0})
            for num in q1_ans:
                for profile in ans_dict:
                    if num in ans_dict[profile]:
                        score_dict[profile] += 1
            unordered_list = list()
            for profile in score_dict:
                unordered_list.append((score_dict[profile], profile))
            ordered_list = list()
            while unordered_list:
                ordered_list.append(max(unordered_list))
                unordered_list.remove(max(unordered_list))
            final_ordered_list = list()
            count = 0
            for item in ordered_list:
                if count < 6:
                    final_ordered_list.append(item[1])
                    count += 1
            return render(request, 'quiz/results.html', context={'profiles':final_ordered_list})
        return render(request, 'quiz/questions.html', context={'form':form})
    else:
        form = QuizForm()
        return render(request, 'quiz/questions.html', context={'form':form})
