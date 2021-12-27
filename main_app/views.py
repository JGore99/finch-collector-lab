from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car, Location, Sighting
from django.contrib.auth.views import LoginView
from .forms import SightingForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required(login_url='/')
def cars_index(request):
  cars = Car.objects.filter(user=request.user)
  return render(request, 'cars/index.html', { 'cars': cars })

@login_required(login_url='/')
def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  locations_car_has_not_been_seen = Location.objects.exclude(id__in = car.locations.all().values_list('id'))
  sighting_form = SightingForm()
  return render(request, 'cars/detail.html', { 
    'car': car, 'sighting_form': sighting_form, 'locations': locations_car_has_not_been_seen
    })

@login_required(login_url='/')
def add_sighting(request, car_id):
  form = SightingForm(request.POST)
  if form.is_valid():
    new_sighting = form.save(commit=False)
    new_sighting = car_id = car_id
    new_sighting.save()
  return redirect('cars_detail', car_id=car_id)

class CarCreate(LoginRequiredMixin, CreateView):
  model = Car
  fields = ['make', 'model', 'description', 'year']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CarUpdate(LoginRequiredMixin, UpdateView):
  model = Car
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['model', 'description', 'year']

class CarDelete(LoginRequiredMixin, DeleteView):
  model = Car
  success_url = '/cars/'

@login_required(login_url='/')
def add_sighting(request, car_id):
  form = SightingForm(request.POST)
  if form.is_valid():
    new_sighting = form.save(commit=False)
    new_sighting.car_id = car_id
    new_sighting.save()
  return redirect('cars_detail', car_id=car_id)

class LocationCreate(LoginRequiredMixin, CreateView):
  model = Location
  fields = '__all__'

class LocationList(LoginRequiredMixin, ListView):
  model = Location

class LocationDetail(LoginRequiredMixin, DetailView):
  model = Location

class LocationUpdate(LoginRequiredMixin, UpdateView):
  model = Location
  fields = ['name', 'color']

class LocationDelete(LoginRequiredMixin, DeleteView):
  model = Location
  success_url = '/locations/' 

@login_required(login_url='/')
def assoc_location(request, car_id, location_id):
  Car.objects.get(id=car_id).locations.add(location_id)
  return redirect('cars_detail', car_id=car_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)