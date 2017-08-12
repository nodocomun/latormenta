# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import AnswerForm
from .models import Answer

def index(request):
    total = Answer.objects.count() - 1
    idx1 = random.randint(0, total)
    idx2 = random.randint(0, total)
    answers = Answer.objects.all()
    context = {'answer1': answers[idx1],
               'answer2': answers[idx2]} 
    return render(request, 'mixit/index.html', context)

def new(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/')
    else:
        form = AnswerForm()
    return render(request, 'mixit/new.html', {'form': form})
