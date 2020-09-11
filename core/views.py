from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
from .models import Loefa
import json
import requests



def index(request):
  show = Loefa.objects.order_by('-total')

    # set the apikey and limit
  apikey = "QJEY0TLRC2Y0"  # test value
  lmt = 20

  # our test search
  search_term = "hacker"

  # get the top 8 GIFs for the search term
  r = requests.get(
      "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

  if r.status_code == 200:
      # load the GIFs using the urls for the smaller GIF sizes
      top_8gifs = json.loads(r.content)
      print("ABAIXO ESTA A DESGRAÇA")
      gif = top_8gifs['results']
      cont = 0

      if show:
        return render(request, 'index.html', {'show':show})
      else:  
        for cont in range (cont, lmt):
          loefa = Loefa.objects.create(like = 0, deslike = 0, total = 0, gif = gif[cont]['media'][0]['gif']['url'])
      
      
  return render(request, 'index.html', {'show':show})
      
def add_like(request, id):
  p = Loefa.objects.get(id=id)

  p.like = int(p.like)+1
  p.total = int(p.total)+1

  p.save()

  return redirect('/') 

def add_deslike(request, id):
  p = Loefa.objects.get(id=id)

  p.like = int(p.like)+1
  p.total = int(p.total)-1

  p.save()
  return redirect('/')  
