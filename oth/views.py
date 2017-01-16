from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import models
from django.contrib import messages
from oth import models
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from facepy import GraphAPI
import datetime
import time

m_level = 1
f_user = ""
last = 100

def index(request):
    user = request.user
    if user.is_authenticated():
        player = models.player.objects.get(user_id=request.user.pk)
        try:
            level = models.level.objects.get(l_number=player.max_level)
            return render(request, 'level.html', {'player': player, 'level': level})
        except:
            global last
            if player.max_level > last:
                return render(request, 'win.html', {'player': player})
            return render(request, 'finish.html', {'player': player})
    return render(request, 'index_page.html')


@login_required
def display(request):
    player = models.player.objects.get(user_id=request.user.pk)
    return render(request, 'display.html', {'player': player})


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        profile = user
        try:
            player = models.player.objects.get(user=profile)
        except:
            player = models.player(user=profile)
            player.name = response.get('name')
            player.timestamp=datetime.datetime.now()
            player.save()
    elif backend.name == 'google-oauth2':
        profile = user
        try:
            player = models.player.objects.get(user=profile)
        except:
            player = models.player(user=profile)
            player.timestamp=datetime.datetime.now()
            player.name = response.get('name')['givenName'] + " " + response.get('name')['familyName']
            player.save()


@login_required
def answer(request):
    ans = ""
    if request.method == 'POST':
        ans = request.POST.get('ans')
    player = models.player.objects.get(user_id=request.user.pk)
    try:
        level = models.level.objects.get(l_number=player.max_level)
    except:
        return render(request, 'finish.html', {'player': player})
    # print answer
    # print level.answer
    if ans == level.answer:
        #print level.answer
        player.max_level = player.max_level + 1
        player.score = player.score + 10
        player.timestamp = datetime.datetime.now()
        level.numuser = level.numuser + 1
        level.accuracy = round(level.numuser/(float(level.numuser + level.wrong)),2)
        level.save()
        #print level.numuser
        # print player.max_level
        global m_level
        global f_user
        # print f_user
        # print m_level
        if m_level < player.max_level:
            m_level = player.max_level
            f_user = player.name
        player.save()
        
        try:
            level = models.level.objects.get(l_number=player.max_level)
            return render(request, 'level_transition.html')
            return render(request, 'level.html', {'player': player, 'level': level})
        except:
            return render(request, 'level_transition.html')
            global last
            if player.max_level > last:
                return render(request, 'win.html', {'player': player}) 
            return render(request, 'finish.html', {'player': player})
    elif ans=="":
        pass

    else:
        level.wrong = level.wrong + 1
        level.save()

        messages.error(request, "Wrong Answer!, Try Again")

    return render(request, 'level.html', {'player': player, 'level': level})


def lboard(request):
    p= models.player.objects.order_by('-score','timestamp')
    cur_rank = 1

    for pl in p:
        pl.rank = cur_rank
        cur_rank += 1


    return render(request, 'lboard.html', {'players': p})

@login_required()
def rules(request):
    return render(request, 'index_page.html')

def getNotif(request):
    newNotif = Notif.objects.all().order_by('-date')[:2]
    data = serializers.serialize('json',newNotif)
    return HttpResponse(data, content_type='application/json')

# def correct(request):
#     return render(request, 'level.html', {'player': player, 'level': level})
