from django.shortcuts import render

class Car:  # Note that parens are optional if not inheriting from another class
  def __init__(self, make, model, description, year):
    self.make = make
    self.model = model
    self.description = description
    self.year = year

cars = [
  Car('Lolo', 'tabby', 'Kinda rude.', 3),
  Car('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Car('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Car('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

# Create your views here.
from django.http import HttpResponse

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cars_index(request):
  return render(request, 'cars/index.html', { 'cars': cars })