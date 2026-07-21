from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name="main"),
    path('entry_overview/', views.entry_overview, name="entry_overview"),
    path('new_entry_location/', views.new_entry_location, name="new_entry_location"),
    path('new_entry_items/<int:location_id>', views.new_entry_items, name="new_entry_items"),
    path('items/', views.ItemsView.as_view(), name='items'),
    path('locations/', views.LocationsView.as_view(), name='locations'),
]