from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dolphin,Toy
from .forms import FeedingForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'
def about(request):
  return render(request, 'about.html')

def dolphins_index(request):
    dolphins = Dolphin.objects.all()
    return render(request, 'dolphins/index.html', { 'dolphins': dolphins })

def dolphins_detail(request, dolphin_id):
    dolphin = Dolphin.objects.get(id=dolphin_id)
    toys_dolphin_doesnt_have = Toy.objects.exclude(id__in = dolphin.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'dolphins/detail.html', {
    'dolphin': dolphin, 'feeding_form': feeding_form, 'toys': toys_dolphin_doesnt_have
    })

class DolphinCreate(CreateView):
  model = Dolphin
  fields = ['name', 'breed', 'description', 'age']
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class DolphinUpdate(UpdateView):
    model = Dolphin
    fields = ['breed', 'description', 'age']

class DolphinDelete(DeleteView):
    model = Dolphin
    success_url = '/dolphins/'
    
def add_feeding(request, dolphin_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.dolphin_id = dolphin_id
        new_feeding.save()
        return redirect('dolphins_detail', dolphin_id=dolphin_id)
    
class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'
    
class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'
  
def assoc_toy(request, dolphin_id, toy_id):
    Dolphin.objects.get(id=dolphin_id).toys.add(toy_id)
    return redirect('dolphins_detail', dolphin_id=dolphin_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('dolphinss_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)