from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import CustomUserForm

class SignUpView(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'accounts/signup.html'


@login_required
def CustomUserEdit(request):
  user = request.user
  if request.method == 'POST':
    form = CustomUserForm(request.POST, instance=user)
    if form.is_valid():
      form.save()
      return redirect("matching:index")
  else:
    form = CustomUserForm(instance=user)
    context = {
      "form":form
    }
    return render(request, 'accounts/edit.html', context)
## クラス版も余裕があれば書く
## ドキュメントも添えて
