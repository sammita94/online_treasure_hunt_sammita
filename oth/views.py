from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import models
from oth import models
m_level = 1
f_user = ""

def index(request):
    user=request.user
    if user.is_authenticated():
	player = models.player.objects.get(user_id=request.user.pk)
	level = models.level.objects.get(l_number= player.max_level)	
	return render(request, 'level.html', {'player': player , 'level': level})
    return render(request, 'index_page.html')

@login_required
def display(request):
    player = models.player.objects.get(user_id=request.user.pk)
    return render(request, 'display.html' , {'player': player })



def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        profile = user
        try:
            player = models.player.objects.get(user=profile)
        except:
            player = models.player(user=profile)
            player.name = response.get('name')
            player.save()

"""def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                play = models.player.objects.get(user_id=request.user.pk)
		level = models.level.objects.get(l_number= play.max_level)
    		return render(request, 'level.html' , {'player': play , 'level': level})
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

   
    else:
        return render(request, 'index.html', {})"""

@login_required
def answer(request):
    if request.method == 'POST':
        answer = request.POST.get('ans')
    player = models.player.objects.get(user_id=request.user.pk)
    try:
        level = models.level.objects.get(l_number=player.max_level)	
        print answer
        print level.answer
        if answer == level.answer:
	   	print level.answer
		player.max_level = player.max_level + 1
	#print player.max_level
		global m_level
		global f_user        
		if m_level<player.max_level:
	    	    m_level=player.max_level
	            f_user = player.name	
	   	    player.save()
	try:	
		level = models.level.objects.get(l_number=player.max_level)
		return render(request, 'level.html' , {'player': player , 'level': level})
	except:
		return render(request, 'finish.html' , {'player': player})
    	return render(request, 'level.html' , {'player': player , 'level': level})
    except:
	return render(request, 'finish.html' , {'player': player})


       
		


