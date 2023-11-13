from django.shortcuts import render
from accounts.models import CustomUser
from .models import DirectMessage
from .forms import DirectMessageForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Q
import datetime

# Create your views here.

def index(request):
  if request.user.is_authenticated:
    if request.user.registration_type == 'mentee':
      objects = CustomUser.objects.filter(registration_type='mentor')
      print("hoge")
      print(len(objects))
    elif request.user.registration_type == 'mentor':
      objects = CustomUser.objects.filter(registration_type='mentee')
      print("hoge")
      print(len(objects))
    else:
      return redirect('accounts:edit')
    context = {
      'objects': objects,
    }
    return render(request, 'matching/index.html', context)
  else:
    return redirect('login')

@login_required
def dm(request, id):
  recipient = CustomUser.objects.get(pk=id)
  if request.method == 'POST':
    form = DirectMessageForm(request.POST)
    if form.is_valid():
      dm = form.save(commit=False)
      dm.sender = request.user
      dm.receiver = recipient
      dm.at = datetime.datetime.now()
      dm.save()
      return redirect('matching:dm', id=id)
  else:
    form = DirectMessageForm()
    messages = DirectMessage.objects.filter(
      Q(sender=request.user, receiver=recipient) | Q(sender=recipient, receiver=request.user)
    ).order_by('at')
    context = {
      "messages": messages,
      "form": form,
      "recipient": recipient
    }
    return render(request, 'matching/dm.html', context)

