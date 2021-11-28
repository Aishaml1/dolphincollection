from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dolphin,Toy
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dolphins_index(request):
    dolphins = Dolphin.objects.all()
    return render(request, 'dolphins/index.html', { 'dolphins': dolphins })

def dolphins_detail(request, dolphin_id):
    dolphin = Dolphin.objects.get(id=dolphin_id)
    feeding_form = FeedingForm()
    return render(request, 'dolphins/detail.html', {
    'dolphin': dolphin, 'feeding_form': feeding_form
    })

class DolphinCreate(CreateView):
    model = Dolphin
    fields = '__all__'
    success_url = '/dolphins/'

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