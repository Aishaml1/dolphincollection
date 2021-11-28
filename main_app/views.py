from django.shortcuts import render
from .models import Dolphin
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dolphins_index(request):
    dolphins = Dolphin.objects.all()
    return render(request, 'dolphins/index.html', { 'dolphins': dolphins })