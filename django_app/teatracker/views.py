from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item, Entry, Location
from .serializers import ItemSerializer, LocationSerializer
from .forms import (
    LocationForm, 
    EntryForm, 
    EntryForLocationForm, 
    ItemForLocationForm,
)
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    return render(request, "teatracker/main.html")

@login_required
def entry_overview(request):
    entries = Entry.objects.all()
    return render(request, "teatracker/entry_overview.html", {"entries": entries})
# def tea_entry(request):
#     locations = None
#     items = None# load all items
#     return render(request, 'blog/blog_home.html', {"posts": posts})

@login_required
def new_entry_location(request):
    locations = Location.objects.all()
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save()
            # post.author = request.user
            # post.published_date = timezone.now()
            # location.save()
            # return redirect('post_detail', pk=post.pk)
    
    location_form = LocationForm()
    return render(
        request, 
        "teatracker/new_entry_location.html", 
        {
            "locations": locations,
            "location_form": location_form,
        }
    )

@login_required
def new_entry_items(request, location_id):
    print(f"location_id in 'new_entry_items': {location_id}")
    if request.method == "POST":
        form = ItemForLocationForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.location = Location.objects.filter(id = location_id)[0]
            item.save()
    items = Item.objects.filter(location__id = location_id)
    item_form = ItemForLocationForm()
    entry_form = EntryForLocationForm()
    entry_form.fields["items"].queryset = Item.objects.filter(location__id = location_id)
    return render(
        request,
        "teatracker/new_entry_items.html",
        {
            "item_form": item_form, 
            "entry_form": entry_form, 
            "location_id": location_id
        }
    )

@login_required
def post_entry(request, location_id):
    if request.method == "POST":
        print(request.POST["items"])
        print("handling POST for 'post_entry'")
        form = EntryForLocationForm(request.POST)
        print(form)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.location = Location.objects.filter(id = location_id)[0]
            entry.created_date = timezone.now()
            print(f"items of entry in 'post_entry': {entry}")
            entry.save()
            form.save_m2m()
            return render(
                request,
                "teatracker/created_entry.html",
                {"entry": entry}
            )
    return render(request, "teatracker/entry_not_created.html")

@login_required
def entry_form(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.created_date = timezone.now()
            entry.save()

    entry_form = EntryForm()
    return render(
        request,
        "teatracker/entry_form.html",
        {
            "entry_form": entry_form,
        }
    )