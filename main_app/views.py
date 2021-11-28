from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dolphin
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
  return render(request, 'dolphins/detail.html', { 'dolphin': dolphin })

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