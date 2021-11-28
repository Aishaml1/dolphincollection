from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Dolphin(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('dolphins_detail', kwargs={'dolphin_id': self.id})

class Feeding(models.Model):
    date = models.DateField('Feeding date')
    meal = models.CharField(
        max_length=1,
		choices=MEALS,
		default=MEALS[0][0]
    )
    dolphin = models.ForeignKey(Dolphin, on_delete=models.CASCADE)

def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Meta:
    ordering = ['-date']

