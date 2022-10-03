

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import generic
from account.forms import UserForm

#class SignUpView(generic.CreateView):
 #   form_class = UserCreationForm
  #  success_url = reverse_lazy('login')
   # template_name = 'registration/signup.html'

def SignUpViewMethod(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()

    return render(request, 'registration/signup.html', {'form': form})
        

