from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

TIMES = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('N', 'Night')
)

class Location(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
      return self.name

  def get_absolute_url(self):
      return reverse("locations_detail", kwargs={"pk": self.id})
  

# Create your models here.
class Car(models.Model):
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  year = models.IntegerField()
  locations = models.ManyToManyField(Location)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.make

  def get_absolute_url(self):
      return reverse("cars_detail", kwargs={"car_id": self.id})
  
  def seen_today(self):
    return self.sighting_set.filter(date=date.today()).count() >= len(TIMES)

class Sighting(models.Model):
  date = models.DateField("Sighting date")
  time = models.CharField(
    max_length=1,
    choices=TIMES,
    default=TIMES[0][0]
  )

  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
      return f"{self.get_time_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
