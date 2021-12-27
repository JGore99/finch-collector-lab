from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('cars/', views.cars_index, name='cars_index'),
  path('cars/<int:car_id>/', views.cars_detail, name='cars_detail'),
  path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
  path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
  path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
  path('cars/<int:car_id>/add_sighting', views.add_sighting, name='add_sighting'),
  path('cars/<int:car_id>/assoc_location/<int:location_id>/', views.assoc_location, name='assoc_location'),
  path('location/create/', views.LocationCreate.as_view(), name='location_create'),
  path('location/<int:pk>/', views.LocationDetail.as_view(), name='locations_detail'),
  path('locations/', views.LocationList.as_view(), name='locations_index'),
  path('locations/<int:pk>/update/', views.LocationUpdate.as_view(), name='locations_update'),
  path('locations/<int:pk>/delete/', views.LocationDelete.as_view(), name='locations_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]